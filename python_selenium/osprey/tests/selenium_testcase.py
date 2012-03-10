from . import testcase

from selenium import webdriver
from pyvirtualdisplay import Display

class TestCase(testcase.TestCase):

    def setUp(self): 
        super(TestCase, self).setUp()
        self.display = Display(visible=0, size=(800, 600))
        self.display.start()
    
    def tearDown(self):
        self.display.stop()
        super(TestCase, self).tearDown()

    def getWebDriver(self):
        return webdriver.Firefox()

