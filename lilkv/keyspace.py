# -*- coding: utf-8 -*-

"""
    lilkv.keyspace

    This module object contains all column families.
"""

import sys

from columnfamily import ColumnFamily


class Keyspace(object):
    """Keyspaces contain a list of column families, along with key
    configuration details.
    """

    KEYSPACES = {}

    def __init__(self, name):
        self.name = name
        Keyspace.KEYSPACES[name] = self
        self.columnfamilies = {}

    def create_columnfamily(self, cf_name):
        cf = ColumnFamily(cf_name)
        self.columnfamilies[cf.name] = cf
        return cf

    def delete_columnfamily(self, cf_name, sure=False):
        if sure:
            del self.columnfamilies[cf_name]
            sys.stdout.write("ColumnFamily %s deleted." % cf_name)
            sys.stdout.flush()
        return

    def __repr__(self):
        return '''Keyspace: %s\n
            \rColumnFamilies: %s\n
            ''' % (self.name, self.columnfamilies)
