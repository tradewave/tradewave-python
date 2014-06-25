import json

from httmock import urlmatch, HTTMock
import tradewave

from .base import BaseTestCase


STRATEGY_DICT = {"public": False,
                 "featured": False,
                 "id": "EdAPcGZmcL",
                 "forked": False,
                 "name": "Test strategy"}


class StrategyTestCase(BaseTestCase):
    def test_strategy(self):
        @urlmatch(path=r'.*strategies/?$')
        def strategy_mock(url, request):
            return {'status_code': 200, 'content': json.dumps([STRATEGY_DICT])}

        with HTTMock(strategy_mock):
            strategies = self.client.strategies()
            self.assertEqual(len(strategies), 1)

            strategy = strategies[0]
            self.assertTrue(isinstance(strategy, tradewave.Strategy))
            for key, value in STRATEGY_DICT.iteritems():
                self.assertEqual(getattr(strategy, key), value)
