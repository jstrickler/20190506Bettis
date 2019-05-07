#!/usr/bin/env python

import unittest

class TestSpam(unittest.TestCase):
    
    def test_one_is_one(self):
        self.assertEqual(1,1)
        
if __name__ == '__main__':
    unittest.main()