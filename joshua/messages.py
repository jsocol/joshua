import json

from tornado import httpclient

from nodes import known_nodes


http_client = httpclient.AsyncHTTPClient()


def hello(local, remote):
    """Say hello to other nodes in the cluster."""
    def _handler(response):
        if response.error:
            print reponse.error
        else:
            import pdb; pdb.set_trace()
    data = json.dumps({'addr': local.addr, 'port': local.port})
    http_client.fetch(remote.url, _handler, method='POST', body=data)
