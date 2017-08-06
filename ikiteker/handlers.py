# -*- coding: utf-8 -*-

from tornado import gen, web
from tornado.escape import json_encode
from ikiteker.services import ISTANBUL_BOUNDS

class HealthCheckHandler(web.RequestHandler):
    def get(self):
        response = { 'status': 'ok' }
        self.set_header('Content-Type', 'application/json')
        self.write(response)


class RidersHandler(web.RequestHandler):
    def initialize(self, rider_service):
       self.rider_service = rider_service

    @gen.coroutine
    def get(self):
        bounds = self.get_argument('bounds', ISTANBUL_BOUNDS)
        result = yield self.rider_service.get_riders(bounds)
        self.set_header('Content-Type', 'application/json')
        self.write(json_encode(result))


