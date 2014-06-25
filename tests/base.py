import unittest

import tradewave


class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.client = tradewave.Client(username='test_user',
                                       token='test_token')
