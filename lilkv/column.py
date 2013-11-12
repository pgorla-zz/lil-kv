# -*- coding: utf-8 -*-

"""
    lilkv.column

    This module implements a single column that is stored in lilkv.
"""

from datetime import datetime


class Column(object):

    """The Column object is the fundamental data storage unit.
    Each Column contains a key, a value, a timestamp, and a TTL.

    :param row_key:
    :param col_name:
    :param value:
    :param timestamp:
    :param TTL:
    """

    def __init__(self, row_key, col_name=None, value=None,
                 timestamp=None, TTL=None, tombstone=False):
        self.timestamp = datetime.now() if timestamp is None else timestamp
        self.row_key = row_key
        self.col_name = col_name
        self.value = value
        self.TTL = TTL
        self.tombstone = tombstone

    def __repr__(self):
        return '%s => %s' % (self.row_key, (self.col_name, self.value))
