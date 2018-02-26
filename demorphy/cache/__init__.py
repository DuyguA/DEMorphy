# -*- coding: utf-8 -*-


__all__ = ["lrudecorator", "lrucache", "memoize"]


from demorphy.cache.pylru import lrudecorator, lrucache
from demorphy.cache.simple_cache import memoize
