from tornado import web
from ikiteker import handlers
from ikiteker.services import RiderService

routes = [
    web.url(r"/health", handlers.HealthCheckHandler),
    web.url(r"/riders", handlers.RidersHandler, kwargs={ 'rider_service': RiderService()})
]
