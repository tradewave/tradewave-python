import six


class BackTest(object):
    """Base class for a Tradewave backtest"""
    def __init__(self,
                 strategy_id,
                 id=None,
                 **kwargs):
        # TODO: validation?
        self.id = id
        self.strategy_id = strategy_id
        for key, value in six.iteritems(kwargs):
            setattr(self, key, value)
