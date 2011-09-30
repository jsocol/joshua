"""Joshua Public Server."""

from tornado import web


class ObjectHandler(web.RequestHandler):
    @web.asynchronous
    def get(self, obj):
        """
        Handle a conditional GET from a browser and return an object or 404.

        If I don't know about an object, query other nodes.

        """
        raise NotImplementedError


public_application = web.Application([
    (r'/(.*)', ObjectHandler),
])
