import osprey.d7.tests.testcase as d7_testcase
import osprey.tests.runner as osprey_runner

class TestMenu(d7_testcase.TestCase):

    def setUp(self):
        super(TestMenu,self).setUp()
        self.menu_xpath = "//div[contains(@class, 'sidebar')]"

    def testAffiliations(self):
        wd = self.getWebDriver()

        #  Go to base url.
        print "Start page: %s" % self.base_url
        wd.get(self.base_url)
        #wd.get_screenshot_as_file('/tmp/foo.png')
        
        # Click affiliations link.
        print "Clicking 'Affiliations' link"
        wd.find_element('xpath', "%s//a[contains(text(), 'Affiliations')]" % self.menu_xpath).click()
        self.assertDrupalErrorNotPresent(wd)
       
        # Click NSF link.
        print "Clicking 'National Science Foundation Link'"
        wd.find_element('xpath', "//table//a[contains(text(),'National Science Foundation')]").click()
        self.assertDrupalErrorNotPresent(wd)

if __name__ == '__main__': 
    osprey_runner.runTestCase(TestMenu)


