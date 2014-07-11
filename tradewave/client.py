import socket
try:
    from urlparse import urljoin
except ImportError:
    from urllib.parse import urljoin

import requests

from tradewave.endpoints.strategy import Strategy
from tradewave.libs.general import parse_response


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

        # instantiate a session and set default headers
        self.session = requests.Session()
        self.session.headers.update({USERNAME_HEADER: self.username,
                                     TOKEN_HEADER: self.token})

    def _request(self, endpoint, method, data=None):
        """Internal method for making HTTP(s) requests"""
        response = self.session.request(method=method,
                                        url=urljoin(self.base_url, endpoint),
                                        params=data,
                                        data=data,
                                        timeout=self.timeout)
        return parse_response(response)

    def strategies(self):
        endpoint = 'strategies/'

        strategies = self._request(endpoint, 'GET')
        return [Strategy(**strategy) for strategy in strategies]

    def create_strategy(self, strategy):
        endpoint = 'strategies/'

        data = strategy.__dict__
        result = self._request(endpoint, 'POST', data)
        strategy.__dict__.update(result)

    def save_strategy(self, strategy):
        endpoint = 'strategies/{id}/edit'.format(id=strategy.id)

        data = strategy.__dict__
        self._request(endpoint, 'POST', data)

    def delete_strategy(self, strategy):
        endpoint = 'strategies/{id}/delete'.format(id=strategy.id)

        self._request(endpoint, 'POST')

    def get_strategy(self):
        # TODO
        pass

    def fork_strategy(self):
        # TODO
        pass
