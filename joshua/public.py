"""Joshua Public Server."""

from datetime import datetime, timedelta
import mimetypes

from tornado import web

from filestore import StoredObject, DoesNotExist


class ObjectHandler(web.RequestHandler):
    @web.asynchronous
    def get(self, obj):
        """
        Handle a conditional GET from a browser and return an object or 404.

        If I don't know about an object, query other nodes.

        """
        name, _, ext = obj.rpartition('.')
        try:
            so = StoredObject(name=name, extension=ext)
        except DoesNotExist:
            # TODO: Ask other nodes about this object.
            self.set_status(404)
            self.finish()
            return

        data = so.read()
        mimetype = mimetypes.guess_type(obj)
        self.set_header('Expires', datetime.now() + timedelta(days=3653))
        self.set_header('X-Joshua-Node', 'my-unique-node-name')
        self.set_header('Content-type', mimetype[0])
        self.write(data)
        self.finish()


public_application = web.Application([
    (r'/(.*)', ObjectHandler),
])
