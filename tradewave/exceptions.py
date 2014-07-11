class TradewaveError(Exception):
    pass


class ResponseError(TradewaveError):
    pass


class ResponseParsingError(ResponseError):
    pass
