class Strategy(object):
    """Base class for a Tradewave strategy"""
    def __init__(self,
                 name,
                 id=None,
                 public=False,
                 featured=False,
                 forked=False):
        self.name = name
        self.id = id
        self.featured = featured
        self.public = public
        self.forked = forked
