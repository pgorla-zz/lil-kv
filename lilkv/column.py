# -*- coding: utf-8 -*-

"""
    lilkv.column

    This module implements a single column that is stored in lilkv.
"""

from datetime import datetime


class Column(object):

    """The Column object is the fundamental data storage unit.
    Each Column contains a key, a value, a timestamp, and a TTL.

    :param key:
    :param value:
    :param timestamp:
    :param TTL:
    """

    def __init__(self, key, value=None, timestamp=None, 
                 TTL=None, tombstone=False):
        self.timestamp = datetime.now() if timestamp is None else timestamp
        self.key = key
        self.value = value
        self.TTL = TTL
        self.tombstone = tombstone

    def __repr__(self):
        return '%s => %s' % (self.key, self.value)
