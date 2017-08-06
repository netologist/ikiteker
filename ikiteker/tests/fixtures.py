from ikiteker.services import ISTANBUL_BOUNDS
from tornado.concurrent import Future

class StravaFixtures:
    def segments_fixture(self, bounds):
        f = Future()
        if bounds == ISTANBUL_BOUNDS:
            f.set_result([
                {
                  "id": 1,
                  "resource_state": 2,
                  "name": "Stamford",
                  "climb_category": 0,
                  "climb_category_desc": "NC",
                  "avg_grade": 0.4,
                  "start_latlng": [
                    40.939863,
                    29.111224
                  ],
                  "end_latlng": [
                    40.935114,
                    29.115105
                  ],
                  "elev_difference": 2.2,
                  "distance": 620.3,
                  "points": "ca{xFcxtpD~PqMzFmExBgB",
                  "starred": False
                }
            ])
        elif bounds == "empty-leaderboard-bounds":
            f.set_result([
                {
                    "id": 2,
                    "resource_state": 2,
                    "name": "Stamford",
                    "climb_category": 0,
                    "climb_category_desc": "NC",
                    "avg_grade": 0.4,
                    "start_latlng": [
                        40.939863,
                        29.111224
                    ],
                    "end_latlng": [
                        40.935114,
                        29.115105
                    ],
                    "elev_difference": 2.2,
                    "distance": 620.3,
                    "points": "ca{xFcxtpD~PqMzFmExBgB",
                    "starred": False
                }
            ])
        elif bounds == "get-multiple-effort-bounds":
            f.set_result([
                {
                    "id": 3,
                    "resource_state": 2,
                    "name": "Death Star",
                    "climb_category": 0,
                    "climb_category_desc": "NC",
                    "avg_grade": 0.4,
                    "start_latlng": [
                        40.939863,
                        29.111224
                    ],
                    "end_latlng": [
                        40.935114,
                        29.115105
                    ],
                    "elev_difference": 2.2,
                    "distance": 8652.9,
                    "points": "ca{xFcxtpD~PqMzFmExBgB",
                    "starred": False
                },
                {
                    "id": 4,
                    "resource_state": 2,
                    "name": "Naboo",
                    "climb_category": 0,
                    "climb_category_desc": "NC",
                    "avg_grade": 0.4,
                    "start_latlng": [
                        40.939863,
                        29.111224
                    ],
                    "end_latlng": [
                        40.935114,
                        29.115105
                    ],
                    "elev_difference": 2.2,
                    "distance": 124.3,
                    "points": "ca{xFcxtpD~PqMzFmExBgB",
                    "starred": False
                },
                {
                    "id": 5,
                    "resource_state": 2,
                    "name": "Kamino",
                    "climb_category": 0,
                    "climb_category_desc": "NC",
                    "avg_grade": 0.4,
                    "start_latlng": [
                        40.939863,
                        29.111224
                    ],
                    "end_latlng": [
                        40.935114,
                        29.115105
                    ],
                    "elev_difference": 2.2,
                    "distance": 124.3,
                    "points": "ca{xFcxtpD~PqMzFmExBgB",
                    "starred": False
                }
            ])
        else:
            f.set_result([])


        return f

    def segment_learderboard_fixture(self, segment_id):
        f = Future()
        if segment_id == 1:
            f.set_result({
              "effort_count": 595,
              "entry_count": 595,
              "neighborhood_count": 1,
              "kom_type": "kom",
              "entries": [
                {
                  "athlete_name": "Tony Stark",
                  "athlete_id": 1,
                  "athlete_gender": "M",
                  "average_hr": 162.9,
                  "average_watts": 398.1,
                  "distance": 12676.4,
                  "elapsed_time": 1023,
                  "moving_time": 1023,
                  "start_date": "2017-07-28T17:18:57Z",
                  "start_date_local": "2017-07-28T20:18:57Z",
                  "activity_id": 1105880839,
                  "effort_id": 27221195631,
                  "rank": 1,
                  "neighborhood_index": 0,
                  "athlete_profile": "https://dgalywyr863hv.cloudfront.net/pictures/athletes/4247004/3500624/2/large.jpg"
                }
              ]
            })
        elif segment_id == 3:
            f.set_result({
              "effort_count": 595,
              "entry_count": 595,
              "neighborhood_count": 1,
              "kom_type": "kom",
              "entries": [
                {
                  "athlete_name": "Anakin Skywalker",
                  "athlete_id": 1,
                  "athlete_gender": "M",
                  "average_hr": 162.9,
                  "average_watts": 398.1,
                  "distance": 12676.4,
                  "elapsed_time": 1023,
                  "moving_time": 1023,
                  "start_date": "2017-07-28T17:18:57Z",
                  "start_date_local": "2017-07-28T20:18:57Z",
                  "activity_id": 1105880839,
                  "effort_id": 27221195631,
                  "rank": 10,
                  "neighborhood_index": 0,
                  "athlete_profile": "https://dgalywyr863hv.cloudfront.net/pictures/athletes/4247004/3500624/2/large.jpg"
                }
              ]
            })
        elif segment_id == 4:
            f.set_result({
              "effort_count": 595,
              "entry_count": 595,
              "neighborhood_count": 1,
              "kom_type": "kom",
              "entries": [
                {
                  "athlete_name": "Anakin Skywalker",
                  "athlete_id": 1,
                  "athlete_gender": "M",
                  "average_hr": 90.9,
                  "average_watts": 398.1,
                  "distance": 12676.4,
                  "elapsed_time": 1023,
                  "moving_time": 1023,
                  "start_date": "2017-07-28T17:18:57Z",
                  "start_date_local": "2017-07-28T20:18:57Z",
                  "activity_id": 1105880839,
                  "effort_id": 27221195631,
                  "rank": 2,
                  "neighborhood_index": 0,
                  "athlete_profile": "https://dgalywyr863hv.cloudfront.net/pictures/athletes/4247004/3500624/2/large.jpg"
                },
                {
                  "athlete_name": "Master Yoda",
                  "athlete_id": 2,
                  "athlete_gender": "M",
                  "average_hr": 162.9,
                  "average_watts": 398.1,
                  "distance": 12676.4,
                  "elapsed_time": 1023,
                  "moving_time": 1023,
                  "start_date": "2017-07-28T17:18:57Z",
                  "start_date_local": "2017-07-28T20:18:57Z",
                  "activity_id": 1105880839,
                  "effort_id": 27221195631,
                  "rank": 1,
                  "neighborhood_index": 0,
                  "athlete_profile": "https://dgalywyr863hv.cloudfront.net/pictures/athletes/4247004/3500624/2/large.jpg"
                }
              ]
            })
        else:
            f.set_result(None)

        return f
