from . import testcase
from . import conf as osprey_conf

import subprocess
import shlex
import time
import socket

from pyvirtualdisplay import Display
from selenium import webdriver

class TestCase(testcase.TestCase):

    def setUp(self): 
        super(TestCase, self).setUp()

        # Start virtual display.
        self.display = Display(visible=0, size=(800, 600))
        self.display.start()

        # Start selenium server in child process.
        selenium_jar = osprey_conf.conf.get('selenium_jar', '')
        null=open('/dev/null')
        self.selenium_proc =subprocess.Popen(shlex.split('java -jar "{p}"'.format(p=selenium_jar)),stdout=null,stderr=null)

        # Try to create webdriver.
        self.wd = None
        try:
            self.wd = webdriver.Remote("http://localhost:4444/wd/hub", webdriver.DesiredCapabilities.FIREFOX)
            #wd = webdriver.Remote("http://localhost:4444/wd/hub", webdriver.DesiredCapabilities.HTMLUNIT)
        except socket.error as err:
            time.sleep(1)
        if not self.wd: raise Exception, "Could not create webdriver."

    def tearDown(self):

        # Stop selenium child process.
        self.selenium_proc.terminate()

        # Stop virtual display.
        self.display.stop()
        super(TestCase, self).tearDown()

    def getWebDriver(self):
        return self.wd

