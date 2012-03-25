from . import testcase
from . import conf as osprey_conf

import subprocess
import shlex
import time
from selenium import webdriver

class TestCase(testcase.TestCase):

    def setUp(self): 
        super(TestCase, self).setUp()

        # Start selenium server in child process.
        selenium_jar = osprey_conf.conf.get('selenium_jar', '')
        null=open('/dev/null')
        self.selenium_proc =subprocess.Popen(shlex.split('java -jar "{p}"'.format(p=selenium_jar)),stdout=null,stderr=null)
        time.sleep(1)
    
    def tearDown(self):
        # Stop selenium child process.
        self.selenium_proc.terminate()
        super(TestCase, self).tearDown()

    def getWebDriver(self):
        wd = webdriver.Remote("http://localhost:4444/wd/hub", webdriver.DesiredCapabilities.HTMLUNIT)
        return wd

