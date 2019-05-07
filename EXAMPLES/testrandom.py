#!/usr/bin/python3
# Test three functions from the random module: 
import random
import unittest

class TestSequenceFunctions(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Starting all tests")

    def setUp(self):
        print("Hello!")
        self.seq = list(range(10))

    def testshuffle(self):
        # make sure the shuffled sequence does not lose any elements
        random.shuffle(self.seq)
        self.seq.sort()
        self.assertEqual(self.seq, list(range(10)))

    def testchoice(self):
        element = random.choice(self.seq)
        self.assertIn(element, self.seq)

    def testsample(self):
        self.assertRaises(ValueError, random.sample, self.seq, 20)
        for element in random.sample(self.seq, 5):
            self.assertIn(element, self.seq)

    def tearDown(self):
        print("Goodbye!")

    @classmethod
    def tearDownClass(cls):
        print("Ending all tests")

if __name__ == '__main__':

    unittest.main()
