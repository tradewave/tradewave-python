import socket

from .base import BaseTestCase
from tradewave import __version__


class ClientTestCase(BaseTestCase):
    username = "test_user"
    token = "test_token"

    def test_default_settings(self):
        self.assertEqual(self.client.timeout, socket.getdefaulttimeout())
        self.assertEqual(self.client.base_url, 'https://tradewave.net/api/')
        self.assertEqual(self.client.username, self.username)
        self.assertEqual(self.client.token, self.token)

        expected_headers = {'X-Tradewave-Username': self.username,
                            'X-Tradewave-Token': self.token,
                            'User-Agent': 'Tradewave-python/%s' % __version__}
        self.assertTrue(set(expected_headers.items()).
                        issubset(set(self.client.session.headers.items())))
