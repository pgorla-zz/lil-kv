# -*- coding: utf-8 -*-

"""
    lilkv.testsuite.basic

    Test lilkv basic functionality.
"""

from lilkv.testsuite import LilKVTestCase

from lilkv.keyspace import Keyspace
from lilkv.columnfamily import ColumnFamily
from lilkv.column import Column


class BasicTests(LilKVTestCase):
    """Baseclass for testing out the application.
    """

    def test_keyspace_creation(self):
        ks = Keyspace("Test Keyspace")
        self.assert_in("Test Keyspace", Keyspace.KEYSPACES)

    def test_columnfamily_creation(self):
        ks = Keyspace("Test Keyspace")
        ks.create_columnfamily("daily_visitors")
        self.assert_in("daily_visitors", ks.columnfamilies)

    def test_adding_data(self):
        pass

    def test_reading_data(self):
        pass

    def test_deleting_data(self):
        pass
