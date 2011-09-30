"""Joshua Node Server."""

import json

from tornado import web


nodes = set()


class HelloHandler(web.RequestHandler):
    """Handshake/introduction messages."""
    def post(self):
        """
        Return all the other nodes I know about, so the newbie can
        introduce itself.

        """
        data = json.loads(self.request.body)
        retval = {'nodes': [n for n in nodes]}
        if data['node'] in nodes:
            self.set_status(304)
        else:
            nodes.add(data['node'])
            self.set_status(200)
        self.write(retval)
        self.finish()


class ObjectHandler(web.RequestHandler):
    def post(self):
        """Learn about a new object from a peer."""
        raise NotImplementedError

    def get(self, obj):
        """Send an object to a peer on demand."""
        raise NotImplementedError

    def delete(self, obj):
        """Learn about a delete from a peer."""
        raise NotImplementedError


class ObjectListHandler(web.RequestHandler):
    def get(self):
        """Return a list of the objects I have."""
        raise NotImplementedError


p2p_application = web.Application([
    (r'/hello', HelloHandler),
    (r'/object(?:/(.*))?', ObjectHandler),
    (r'/objects', ObjectListHandler),
])
