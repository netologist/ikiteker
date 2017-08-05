# -*- coding: utf-8 -*-

import httplib

from tornado import web
from tornado import escape
from tornado import testing
from hamcrest import *

from ikiteker import *

class HealthCheckHandlerTest(testing.AsyncHTTPTestCase):
    def test_should_return_healthcheck_endpoint_success_result(self):
        response = self.fetch(
            '/health',
            method='GET'
        )
        expectedJsonResponse = { 'status': u'ok' }

        assert_that(response.code, is_(httplib.OK))
        assert_that(response.headers, has_entry('Content-Type', contains_string('application/json')))
        assert_that(escape.json_decode(response.body), is_(dict(expectedJsonResponse)))

    def get_app(self):
        return application
