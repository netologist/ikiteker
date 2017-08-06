import os
from tornado import web
from tornado import ioloop
from tornado import httpserver
from ikiteker.routes import *

def main():
    application = web.Application(routes)
    http_server = httpserver.HTTPServer(application)
    ikiteker_port = int(os.environ.get("IKITEKER_PORT", 5000))
    port = int(os.environ.get("PORT", ikiteker_port))
    http_server.listen(port)
    ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
