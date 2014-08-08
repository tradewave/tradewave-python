from .client import Client
from .endpoints.strategy import Strategy
from .endpoints.backtest import BackTest


try:
    __version__ = __import__('pkg_resources') \
        .get_distribution('tradewave').version
except:
    __version__ = 'unknown'

__all__ = ['Client', 'Strategy', 'BackTest']
