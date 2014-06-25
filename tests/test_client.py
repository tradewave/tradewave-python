import socket

from .base import BaseTestCase


class ClientTestCase(BaseTestCase):
    def test_default_timeout(self):
        self.assertEqual(self.client.timeout, socket.getdefaulttimeout())
