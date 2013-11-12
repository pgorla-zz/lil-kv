# -*- coding: utf-8 -*-

"""
    lilkv.testsuite

    Tests lilkv app.
"""

import unittest


class LilKVTestCase(unittest.TestCase):
    """Baseclass for all tests that lilkv uses. Use these methods
    for testing instead of the camelcased ones in the baseclass for
    consistency. Modeled very closely to flask.testsuite.FlaskTestCase.
    """

    def setup(self):
        pass

    def teardown(self):
        pass

    def setUp(self):
        self.setup()

    def tearDown(self):
        unittest.TestCase.tearDown(self)
        self.teardown()

    def assert_equal(self, x, y):
        return self.assertEqual(x, y)

    def assert_raises(self, exc_type, callable=None, *args, **kwars):
        raise Exception("Function not implemented.")

    def assert_true(self, x, msg=None):
        self.assertTrue(x, msg)

    def assert_false(self, x, msg=None):
        self.assertFalse(x, msg)

    def assert_in(self, x, y):
        self.assertIn(x, y)

    def assert_not_in(self, x, y):
        self.assertNotIn(x, y)
