import optparse

from tornado import ioloop

from client import client_application
from conf import settings
from node import p2p_application
from public import public_application


if __name__ == '__main__':
    # TODO: Non-CLI configuration.
    parser = optparse.OptionParser()
    parser.add_option('-n', '--n2n', type='int', default=8888,
                      help='N2N port')
    parser.add_option('-p', '--public', type='int', default=8000,
                      help='Public port')
    parser.add_option('-c', '--client', type='int', default=3000,
                      help='Client port')
    parser.add_option('-f', '--files', default='/tmp/joshua',
                      help='Where to keep uploaded files')

    (opts, _) = parser.parse_args()


    # TODO: Wrap this. Or maybe make joshua.server contain this part and move
    # other startup into a different module.
    p2p_application.listen(settings.P2P_PORT)
    public_application.listen(settings.PUBLIC_PORT)
    client_application.listen(settings.CLIENT_PORT)
    ioloop.IOLoop.instance().start()
