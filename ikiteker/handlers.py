# -*- coding: utf-8 -*-

from datetime import date
import tornado.escape
import tornado.ioloop
import tornado.web

class HealthCheckHandler(tornado.web.RequestHandler):
    def get(self):
        config = ConfigParser.RawConfigParser(allow_no_value=True)
        response = { 'status': 'ok' }
        self.set_header('Content-Type', 'application/json')
        self.write(response)



