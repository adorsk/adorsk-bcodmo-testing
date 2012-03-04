import osprey.tests.testcase as osprey_testcase

from . import conf as d7_conf

class TestCase(osprey_testcase.TestCase):

    def setUp(self):
        self.base_url = d7_conf.conf['base_url']

    def assertDrupalError(self): pass

    
    def tearDown(self): pass




