"""Joshua Client-to-Node Server."""

from tornado import web

from filestore import StoredObject, DoesNotExist


class ObjectHandler(web.RequestHandler):

    @web.asynchronous
    def get(self, obj):
        """Return metadata about an object.

        If I don't know about an object, ask other nodes.

        """
        raise NotImplementedError

    def post(self, obj):
        """Take data for a new object. Return its unique identifier.

        After the data is stored, share the new object with other nodes.

        """
        _, _, ext = obj.rpartition('.')
        so = StoredObject(extension=ext)
        data = self.request.body
        so.write(data)
        self.set_status(200)
        self.write({
            'status': 'OK',
            'name': u'.'.join([so.name, so.extension])
        })
        # TODO: Alert other nodes about this file.

    def delete(self, obj):
        """Delete an object.

        If the delete is successful, return an OK and alert other nodes.

        """
        name, _, ext = obj.rpartition('.')
        try:
            so = StoredObject(name=name, extension=ext)
        except DoesNotExist:
            self.set_status(404)
            self.finish()
            return

        so.delete()
        self.set_status(200)
        self.write({
            'status': 'OK',
        })
        self.finish()
        # TODO: Alert other nodes about this delete.


client_application = web.Application([
    (r'/object(?:/(.*))?', ObjectHandler),
])
