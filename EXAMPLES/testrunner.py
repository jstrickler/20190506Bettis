#!/usr/bin/env python

import unittest
from testspam import TestSpam
from testeggs import TestEggs

# create an empty test suite
testall_suite = unittest.TestSuite()

# create test suites from TestSpam and TestEggs
spam_suite = unittest.makeSuite(TestSpam)
eggs_suite = unittest.makeSuite(TestEggs)

# add suites from TestSpam and TestEggs to the testall suite
testall_suite.addTest(spam_suite)
testall_suite.addTest(eggs_suite)

# create a generic test runner whose output goes to the screen
runner = unittest.TextTestRunner()

# uncomment for more details
runner = unittest.TextTestRunner(verbosity=2)

# run the suite of suites
runner.run(testall_suite)