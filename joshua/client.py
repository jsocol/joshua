"""Joshua Client-to-Node Server."""

from tornado import web


class ObjectHandler(web.RequestHandler):

    @web.asynchronous
    def get(self, obj):
        """Return metadata about an object.

        If I don't know about an object, ask other nodes.

        """
        raise NotImplementedError

    def post(self):
        """Take data for a new object. Return its unique identifier.

        After the data is stored, share the new object with other nodes.

        """
        raise NotImplementedError

    def delete(self, obj):
        """Delete an object.

        If the delete is successful, return an OK and alert other nodes.

        """
        raise NotImplementedError


client_application = web.Application([
    (r'/object(?:/(.*))?', ObjectHandler),
])
