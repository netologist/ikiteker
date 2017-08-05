import os
from tornado import web
from tornado import ioloop
from tornado import httpserver
from ikiteker.routes import *

def main():
    application = web.Application(routes)
    http_server = httpserver.HTTPServer(application)
    port = int(os.environ.get("IKITEKER_PORT", 5000))
    http_server.listen(port)
    ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
