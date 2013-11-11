# -*- coding: utf-8 -*-

"""
    lilkv.row

    This module defines a row in the key-value structure.

"""


class Row(object):
    """A collection of related columns, bound together by a single
    row-key. Each row can contain up to 1000 columns.
    """

    def __init__(self):
        self.columns = {}

    def add(self, Column):
        self.columns[Column.key] = Column

    def get(self, key):
        try:
            return self.columns[key].value
        except Exception:
            raise Exception("Key not found.")
