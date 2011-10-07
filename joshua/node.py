"""Joshua Node Server."""

import json

from tornado import web

from nodes import Node, known_nodes


class HelloHandler(web.RequestHandler):
    """Handshake/introduction messages."""
    def post(self):
        """
        Return all the other nodes I know about, so the newbie can
        introduce itself.

        """
        print 'Got handshake'
        data = json.loads(self.request.body)
        node = Node(addr=data['addr'], port=data['port'])
        if node in known_nodes:
            self.set_status(304)
        else:
            known_nodes.add(node)
            self.set_status(200)
        nodes = [dict(addr=n.addr, port=n.port) for n in known_nodes]
        self.write(json.dumps({'nodes': nodes}))
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
