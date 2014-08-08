import socket

try:
    from urlparse import urljoin
except ImportError:
    from urllib.parse import urljoin

import requests

from .endpoints.backtest import BackTest
from .endpoints.strategy import Strategy
from .libs.general import parse_response

try:
    version = __import__('pkg_resources') \
        .get_distribution('tradewave').version
except:
    version = 'unknown'


API_ENDPOINT = 'https://tradewave.net/api/'
USERNAME_HEADER_NAME = 'X-Tradewave-Username'
TOKEN_HEADER_NAME = 'X-Tradewave-Token'
USER_AGENT_HEADER_VALUE = 'Tradewave-python/%s' % version


class Client(object):
    """A python interface into the Tradewave API"""

    def __init__(self, username, token, base_url=None, timeout=None):
        self.username = username
        self.token = token
        self.base_url = base_url or API_ENDPOINT
        self.timeout = timeout or socket.getdefaulttimeout()

        # instantiate a session and set default headers
        self.session = requests.Session()
        self.session.headers.update({USERNAME_HEADER_NAME: self.username,
                                     TOKEN_HEADER_NAME: self.token,
                                     'User-Agent': USER_AGENT_HEADER_VALUE})

    def _request(self, endpoint, method, data=None):
        """Internal method for making HTTP(s) requests"""
        response = self.session.request(method=method,
                                        url=urljoin(self.base_url, endpoint),
                                        params=data,
                                        data=data,
                                        timeout=self.timeout)
        return parse_response(response)

    # strategies
    def strategies(self):
        endpoint = 'strategies/'

        strategies = self._request(endpoint, 'GET')
        return [Strategy(**strategy) for strategy in strategies]

    def get_strategy(self, strategy_id):
        endpoint = 'strategies/{id}'.format(id=strategy_id)

        strategy = self._request(endpoint, 'GET')
        return Strategy(**strategy)

    def create_strategy(self, strategy):
        endpoint = 'strategies/'

        data = strategy.__dict__
        result = self._request(endpoint, 'POST', data)
        strategy.__dict__.update(result)

    def save_strategy(self, strategy):
        endpoint = 'strategies/{id}/edit'.format(id=strategy.id)

        data = strategy.__dict__
        self._request(endpoint, 'POST', data)

    def delete_strategy(self, strategy_id):
        endpoint = 'strategies/{id}/delete'.format(id=strategy_id)

        self._request(endpoint, 'POST')

    # backtests
    def create_backtest(self, backtest):
        endpoint = 'backtests/'

        data = backtest.__dict__
        result = self._request(endpoint, 'POST', data)
        backtest.__dict__.update(result)

    def last_backtest(self, strategy_id):
        endpoint = 'strategies/{id}/last_backtest'.format(id=strategy_id)

        backtest = self._request(endpoint, 'GET')
        return BackTest(**backtest)
