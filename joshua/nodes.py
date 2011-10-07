"""Global manager of known Joshua nodes."""

class Node(object):
    def __init__(self, addr='127.0.0.1', port=8888):
        self.addr = addr
        self.port = port

    def __str__(self):
        return ':'.join((self.addr, str(self.port)))

    def __repr__(self):
        return '<Node %s>' % self.__str__()

    def __eq__(self, other):
        return (self.addr == other.addr and self.port == other.port)

    def __ne__(self, other):
        return not self.__eq__(other)

    @property
    def url(self):
        return 'http://' + self.__str__()


class NodeSet(object):
    def __init__(self, *a):
        self._nodes = set()
        for n in a:
            self.add(n)

    def __contains__(self, item):
        for n in self._nodes:
            if item == n:
                return True
        return False

    def add(self, item):
        if item not in self:
            self._nodes.add(item)

    def discard(self, item):
        self._nodes.discard(item)

    def remove(self, item):
        self._nodes.remove(item)

    def __repr__(self):
        return '<NodeSet [%s]>' % ', '.join(str(n) for n in self._nodes)

    def __len__(self):
        return len(self._nodes)

    def __iter__(self):
        return self._nodes.__iter__()


known_nodes = NodeSet()
