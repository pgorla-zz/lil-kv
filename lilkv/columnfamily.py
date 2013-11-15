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
        # A row consists of:
        # {'rowkey': [col1, col2, col3]}
        self.ROWS = dict()

    def insert(self, column):
        return self._insert(column)

    def delete(self, column):
        column.tombstone = True
        return self._insert(column)

    def get(self, key):
        # NOTE: Check for tombstones / TTL here
        pass

    def _insert(self, column):
        try:
            self.ROWS[column.row_key].append(column)
            return True
        except KeyError: # Key doesn't exist
            self.ROWS[column.row_key] = [column]
        except:
            return False

    def __repr__(self):
        return '<%r>' % self.name
