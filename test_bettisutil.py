#!/usr/bin/env python
import unittest   # TestCase
from nnl.bettis.misc.bettisutil import spam, eels


class TestBettisutil(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        # common code....
        self.result = spam()

    def test_spam_returns_spam(self):
        self.assertEqual(self.result, "spam")

    def test_spam_rejects_arguments(self):
        with self.assertRaises(TypeError):
            spam(None)

    def test_eels_returns_42(self):
        result = eels()
        self.assertEqual(42, result)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()


