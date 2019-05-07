#!/usr/bin/env python

import unittest

class TestEggs(unittest.TestCase):
    
    def test_two_plus_two_is_four(self):
        self.assertEqual(2 + 2, 4)
        
if __name__ == '__main__':
    unittest.main()