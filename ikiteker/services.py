import os
import logging
from functools import partial
from itertools import chain, groupby
from operator import is_not

from tornado import gen
from tornado.httpclient import AsyncHTTPClient, HTTPRequest
from tornado.httputil import url_concat
from tornado.escape import json_decode
from ikiteker.utils import merge_dict

STRAVA_API_URL = "https://www.strava.com/api/v3"
ISTANBUL_BOUNDS = "40.811404,28.595554,41.199239,29.4288049"

class StravaService:
    def __init__(self, http_client=AsyncHTTPClient()):
        self.http_client = http_client
        self.access_key = os.environ.get("IKITEKER_STRAVA_ACCESS_KEY", "N/A")

    @gen.coroutine
    def get_segments(self, bounds, activity_type='riding'):
        try:
            response = yield self._apiCall("GET", "/segments/explore", {'bounds': bounds, 'activity_type': activity_type})
            if (response.code is not 200):
                logging.error("strava api segments endpoint returns status code "+str(response.code))
                return list()

            json = json_decode(response.body)
            return list(json['segments'])
        except Exception as e:
            logging.error("strava api segments endpoint returns a error")
            logging.error(e)
            return list()


    @gen.coroutine
    def get_segment_leaderboard(self, segment_id):
        logging.debug("segment_id (%d) requested for leaderboard enpoint", segment_id)
        try:
            response = yield self._apiCall("GET", "/segments/"+str(segment_id)+"/leaderboard", {'per_page': 50})
            if (response.code is not 200):
                logging.error("strava api segment leaderboards endpoint returns status code "+str(response.code))
                return None

            json = json_decode(response.body)
            return dict(json)
        except Exception as e:
            logging.error("strava api segments endpoint returns a error")
            logging.error(e)
            return None

    @gen.coroutine
    def _apiCall(self, method, uri, params=None):
        request = HTTPRequest(
            url=url_concat(STRAVA_API_URL + uri, params),
            method=method,
            headers={'Authorization': 'Bearer '+ self.access_key}
        )
        response = yield self.http_client.fetch(request)
        return response



class RiderService:
    def __init__(self, strava_service=StravaService()):
        self.strava_service = strava_service

    @gen.coroutine
    def get_riders(self, bounds):
        segments = yield self.strava_service.get_segments(bounds)
        entries = yield [self.strava_service.get_segment_leaderboard(segment['id']) for segment in segments]
        segments_with_entries = list(map(self._merge_segment, zip(segments, entries)))

        # FlatMap For All Entries
        flatten = list(chain.from_iterable(segments_with_entries))
        flatten_sorted = sorted(flatten, key=lambda b: b['athlete_id'])
        riders = []
        for k, g in groupby(flatten_sorted, lambda b: b['athlete_id']):
            entries = list(g)
            rider = self._create_rider(entries[0])
            rider['efforts'] = self._create_rider_efforts(entries)
            rider['effort_size'] = len(rider['efforts'])
            riders.append(rider)
        return riders

    def _create_rider(self, entry):
        return {
            'id': entry['athlete_id'],
            'name': entry['athlete_name'],
            'profile': entry['athlete_profile'],
            'gender': entry['athlete_gender'],
            'efforts': []
        }

    def _create_rider_effort(self, entry):
        entry.pop('athlete_id', None)
        entry.pop('athlete_name', None)
        entry.pop('athlete_profile', None)
        entry.pop('athlete_gender', None)
        return entry

    def _create_rider_efforts(self, entries):
        return list(map(self._create_rider_effort, entries))


    def _merge_segment(self, tuple):
        segment, board = tuple
        if not board:
            logging.info("board not found for segment_id: %d", segment['id'])
            return list()

        info = {
            'segment': {
                'id': segment['id'],
                'name': segment['name'],
                'distance': segment['distance'],
                'avg_grade': segment['avg_grade'],
                'effort_count': board['effort_count'],
                'entry_count': board['entry_count']
            }
        }

        return list(map(lambda e: merge_dict(e, info), board['entries']))
