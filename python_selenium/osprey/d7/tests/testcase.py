import osprey.tests.selenium_testcase as osprey_selenium_testcase
from . import conf as d7_conf

class TestCase(osprey_selenium_testcase.TestCase):

    def setUp(self):
        super(TestCase,self).setUp()
        self.base_url = d7_conf.conf['base_url']

    def assertDrupalErrorNotPresent(self,webdriver):
        self.assertTrue(len(webdriver.find_elements('css', "div.messages.error")) == 0)
    
    def tearDown(self):
        super(TestCase, self).tearDown()

        




