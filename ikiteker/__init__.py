# -*- coding: utf-8 -*-

__doc__ = u'Tornado REST API for IkiTeker'
__author__ = u'Hasan Ozgan'
__email__ = 'hasanozgan@gmail.com'
__version__ = '0.1.0'

from tornado import web
from tornado import ioloop
from ikiteker import handlers

application = web.Application([
    (r"/health", handlers.HealthCheckHandler)
])

if __name__ == "__main__":
    application.listen(8888)
    ioloop.IOLoop.instance().start()

