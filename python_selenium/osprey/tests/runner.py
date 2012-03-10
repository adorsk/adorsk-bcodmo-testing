"""
Method for running tests.
We do this here so that we can decouple tests from unittest,
and to centralize test running settings.
E.g. for using XML output for all tests.
"""

import unittest
from . import conf as osprey_conf

def runTestCase(test_case, runner=None): 
    suite = unittest.TestLoader().loadTestsFromTestCase(test_case)

    # Set default runner if none was given.
    if not runner: runner = getDefaultRunner()

    runner.run(suite)

def getDefaultRunner():
    return osprey_conf.conf.get('default_runner', unittest.TextTestRunner(verbosity=2))
