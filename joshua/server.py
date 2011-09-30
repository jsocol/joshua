import optparse

from tornado import ioloop

from client import client_application
from node import p2p_application
from public import public_application


if __name__ == '__main__':
    parser = optparse.OptionParser()

    parser.add_option('-n', '--n2n', type='int', default=8888,
                      help='N2N port')
    parser.add_option('-p', '--public', type='int', default=8000,
                      help='Public port')
    parser.add_option('-c', '--client', type='int', default=3000,
                      help='Client port')

    (opts, _) = parser.parse_args()

    p2p_application.listen(opts.n2n)
    public_application.listen(opts.public)
    client_application.listen(opts.client)
    ioloop.IOLoop.instance().start()
