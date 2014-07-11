import requests

try:
    import ujson as json
except ImportError:
    try:
        import simplejson as json
    except ImportError:
        import json

from tradewave.exceptions import ResponseError, ResponseParsingError


def parse_response(response):
    """Analyses and parses JSON response"""
    # TODO: check for mime-type?
    # handle different response status codes
    if response.status_code == 400:
        data = json.loads(response.content)
        error = data.get('error', 'Unknown Error')
        raise ResponseError(error)
    elif response.status_code != requests.codes.ok:
        raise ResponseError(
            'Unexpected response status code: {code}, '
            'reason: {reason}'.format(code=response.status_code,
                                      reason=response.reason))

    # parse response into JSON
    if response.content:
        try:
            return json.loads(response.content)
        except ValueError as e:
            raise ResponseParsingError(*e.args)
    else:
        return ''
