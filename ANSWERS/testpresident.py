#!/usr/bin/python

import unittest
from president import President

class TestPresident(unittest.TestCase):

    def test_president_one_last_name_is_washington(self):
        p = President(1)
        self.assertEqual(p.last_name, "Washington")

    # add other tests here...

if __name__ == '__main__':

    unittest.main()
