import socket
try:
    import ujson as json
except ImportError:
    try:
        import simplejson as json
    except ImportError:
        import json

import requests

from .endpoints.strategy import Strategy


API_ENDPOINT = 'https://tradewave.net/api/'
USERNAME_HEADER = 'X-Tradewave-Username'
TOKEN_HEADER = 'X-Tradewave-Token'


class Client(object):
    """A python interface into the Tradewave API"""
    def __init__(self, username, token, base_url=None, timeout=None):
        self.username = username
        self.token = token
        self.base_url = base_url or API_ENDPOINT
        self.timeout = timeout or socket.getdefaulttimeout()

    def strategies(self):
        # TODO: extract
        headers = {USERNAME_HEADER: self.username,
                   TOKEN_HEADER: self.token}
        endpoint = 'strategies'
        response = requests.get(self.base_url + endpoint, headers=headers)
        strategies = json.loads(response.content)
        return [Strategy(**strategy) for strategy in strategies]
