import unittest

import tradewave


class BaseTestCase(unittest.TestCase):
    username = 'test_user'
    token = 'test_token'

    def setUp(self):
        self.client = tradewave.Client(username=self.username,
                                       token=self.token)
