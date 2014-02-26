# -*- coding: utf-8 -*-

from merkletree import MerkleTree

"""
    lilkv.columnfamily

    This module implements the client-facing aspect of the `lilkv` app. All
    requests are handled through this interface.
"""


class ColumnFamily(object):
    """Column Family objects store information about all rows.

    daily_purchases_cf = ColumnFamily("daily_purchases")
    """

    def __init__(self, name):
        self.name = name

    def insert(self, column):
        pass

    def delete(self, column):
        pass

    def get(self, key):
        # NOTE: Check for tombstones / TTL here
        pass

    def __repr__(self):
        return '<%r>' % self.name

    def cmp(self, cf_b):
        pass
