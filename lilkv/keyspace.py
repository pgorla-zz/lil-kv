# -*- coding: utf-8 -*-

"""
    lilkv.keyspace

    This module object contains all column families.
"""


class Keyspace(object):
    """Keyspaces contain a list of column families, along with key
    configuration details.
    """
    KEYSPACES = {}

    def __init__(self, name):
        KEYSPACES[name] = self
        self.columnfamilies = {}

    def add_columnfamily(self, cf):
        self.columnfamilies[cf.name] = cf
