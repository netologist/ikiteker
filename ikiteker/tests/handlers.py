# -*- coding: utf-8 -*-

from unittest.mock import Mock

from ikiteker.tests.fixtures import StravaFixtures
from tornado import escape
from tornado import testing
from hamcrest import *
from ikiteker.routes import *
from ikiteker.services import *
from ikiteker import handlers


class HealthCheckHandlerTest(testing.AsyncHTTPTestCase):
    def test_should_return_healthcheck_endpoint_success_result(self):
        response = self.fetch(
            '/health',
            method='GET'
        )
        expected_json_response = { 'status': u'ok' }

        assert_that(response.code, is_(200))
        assert_that(response.headers, has_entry('Content-Type', contains_string('application/json')))
        assert_that(escape.json_decode(response.body), is_(dict(expected_json_response)))

    def get_app(self):
        return web.Application([
            web.url(r"/health", handlers.HealthCheckHandler),
        ])

class RiderHandlerTest(testing.AsyncHTTPTestCase):
    def test_should_return_riders_when_request_riders_endpoint(self):
        expected_json_response = [{'id': 1,
                                   'name': 'Tony Stark',
                                   'profile': 'https://dgalywyr863hv.cloudfront.net/pictures/athletes/4247004/3500624/2/large.jpg',
                                   'gender': 'M',
                                   'effort_size': 1,
                                   'efforts': [{
                                       'neighborhood_index': 0,
                                       'rank': 1,
                                       'average_hr': 162.9,
                                       'average_watts': 398.1,
                                       'start_date': '2017-07-28T17:18:57Z',
                                       'moving_time': 1023, 'elapsed_time': 1023,
                                       'activity_id': 1105880839,
                                       'distance': 12676.4,
                                       'effort_id': 27221195631,
                                       'start_date_local': '2017-07-28T20:18:57Z',
                                       'segment': {
                                           'distance': 620.3,
                                           'id': 1,
                                           'name': 'Stamford',
                                           'avg_grade': 0.4,
                                           'entry_count': 595,
                                           'effort_count': 595
                                       }
                                   }]
                                }]

        response = self.fetch(
            '/riders',
            method='GET'
        )
        assert_that(response.code, is_(200))
        assert_that(response.headers, has_entry('Content-Type', contains_string('application/json')))
        assert_that(escape.json_decode(response.body), is_(list(expected_json_response)))

    def test_should_return_empty_json_when_requested_riders_endpoint_with_invalid_bounds(self):
        expected_json_response = []

        response = self.fetch(
            '/riders?bounds=invalid-bounds',
            method='GET'
        )
        assert_that(response.code, is_(200))
        assert_that(response.headers, has_entry('Content-Type', contains_string('application/json')))
        assert_that(escape.json_decode(response.body), is_(list(expected_json_response)))

    def test_should_return_empty_json_when_requested_riders_endpoint_with_empty_leaderboard_bounds(self):
        expected_json_response = []

        response = self.fetch(
            '/riders?bounds=empty-leaderboard-bounds',
            method='GET'
        )
        assert_that(response.code, is_(200))
        assert_that(response.headers, has_entry('Content-Type', contains_string('application/json')))
        assert_that(escape.json_decode(response.body), is_(list(expected_json_response)))

    def test_should_return_empty_json_when_requested_riders_endpoint_with_multiple_effort_bounds(self):
        expected_json_response = [
           {
              'name':'Anakin Skywalker',
              'id':1,
              'gender':'M',
              'profile':'https://dgalywyr863hv.cloudfront.net/pictures/athletes/4247004/3500624/2/large.jpg',
              'efforts':[
                 {
                    'average_hr':162.9,
                    'effort_id':27221195631,
                    'segment':{
                       'name':'Death Star',
                       'entry_count':595,
                       'distance':8652.9,
                       'avg_grade':0.4,
                       'effort_count':595,
                       'id':3
                    },
                    'elapsed_time':1023,
                    'distance':12676.4,
                    'start_date_local':'2017-07-28T20:18:57Z',
                    'start_date':'2017-07-28T17:18:57Z',
                    'average_watts':398.1,
                    'rank':10,
                    'neighborhood_index':0,
                    'activity_id':1105880839,
                    'moving_time':1023
                 },
                 {
                    'average_hr':90.9,
                    'effort_id':27221195631,
                    'segment':{
                       'name':'Naboo',
                       'entry_count':595,
                       'distance':124.3,
                       'avg_grade':0.4,
                       'effort_count':595,
                       'id':4
                    },
                    'elapsed_time':1023,
                    'distance':12676.4,
                    'start_date_local':'2017-07-28T20:18:57Z',
                    'start_date':'2017-07-28T17:18:57Z',
                    'average_watts':398.1,
                    'rank':2,
                    'neighborhood_index':0,
                    'activity_id':1105880839,
                    'moving_time':1023
                 }
              ],
              'effort_size':2
           },
           {
              'name':'Master Yoda',
              'id':2,
              'gender':'M',
              'profile':'https://dgalywyr863hv.cloudfront.net/pictures/athletes/4247004/3500624/2/large.jpg',
              'efforts':[
                 {
                    'average_hr':162.9,
                    'effort_id':27221195631,
                    'segment':{
                       'name':'Naboo',
                       'entry_count':595,
                       'distance':124.3,
                       'avg_grade':0.4,
                       'effort_count':595,
                       'id':4
                    },
                    'elapsed_time':1023,
                    'distance':12676.4,
                    'start_date_local':'2017-07-28T20:18:57Z',
                    'start_date':'2017-07-28T17:18:57Z',
                    'average_watts':398.1,
                    'rank':1,
                    'neighborhood_index':0,
                    'activity_id':1105880839,
                    'moving_time':1023
                 }
              ],
              'effort_size':1
           }
        ]

        response = self.fetch(
            '/riders?bounds=get-multiple-effort-bounds',
            method='GET'
        )
        assert_that(response.code, is_(200))
        assert_that(response.headers, has_entry('Content-Type', contains_string('application/json')))
        assert_that(escape.json_decode(response.body), is_(list(expected_json_response)))

    def get_app(self):
        return web.Application([
            web.url(r"/riders", handlers.RidersHandler, kwargs={ 'rider_service': RiderService(self._create_strava_service())})
        ])

    def _create_strava_service(self):
        fixtures = StravaFixtures()
        strava_service = Mock(spec=StravaService)
        strava_service.get_segments.side_effect = fixtures.segments_fixture
        strava_service.get_segment_leaderboard.side_effect = fixtures.segment_learderboard_fixture

        return strava_service
