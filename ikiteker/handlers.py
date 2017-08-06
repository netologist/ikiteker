# -*- coding: utf-8 -*-

from datetime import date
import tornado.escape
import tornado.ioloop
import tornado.web

class HealthCheckHandler(tornado.web.RequestHandler):
    def get(self):
        response = { 'status': 'ok' }
        self.set_header('Content-Type', 'application/json')
        self.write(response)



