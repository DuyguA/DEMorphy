# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals


def memoize(f):
    """ 
    Caching decorator works for functions with only one argument.
    Simply limitless cache
    """
    class memodict(dict):
        def __missing__(self, key):
            ret = self[key] = f(key)
            return ret 
    return memodict().__getitem__
