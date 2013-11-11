# -*- coding: utf-8 -*-

"""
    lilkv.columnfamily

    This module implements the client-facing aspect of the `lilkv` app. All
    requests are handled through this interface.
"""


class ColumnFamily(object):
    """Column Family objects store information about all rows.

    daily_purchases_cf = ColumnFamily("daily_purchases")
    """

    def __init__(self, name, data_dir='data'):
        self.name = name
        pass

    def insert(self, Column):
        pass

    def get(self, key):
        # NOTE: Check for tombstones / TTL here
        pass

    def delete(self, key):
        # NOTE: Really an insert with a tombstone
        insert(key, tombstone=True)
        pass

    def __repr__(self):
        return '<%r>' % self.name
