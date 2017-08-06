import os
import logging
from tornado import ioloop
from tornado import httpserver
from ikiteker.routes import *

logging.basicConfig() # you need to initialize logging, otherwise you will not see anything from requests
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True

def main():
    application = web.Application(routes)
    http_server = httpserver.HTTPServer(application)
    ikiteker_port = int(os.environ.get("IKITEKER_PORT", 5000))
    port = int(os.environ.get("PORT", ikiteker_port))
    http_server.listen(port)
    ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
