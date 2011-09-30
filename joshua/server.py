from tornado import ioloop

from client import client_application
from node import p2p_application
from public import public_application


if __name__ == '__main__':
    p2p_application.listen(8888)
    public_application.listen(8000)
    client_application.listen(3000)
    ioloop.IOLoop.instance().start()
