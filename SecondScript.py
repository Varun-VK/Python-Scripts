from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import unittest

class Test_PythonOrg(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		sleep(4)
		self.browser.close()
		self.browser = None
    
    def test_02_SignInWorks(self):
		"Test to make sure that Sign In page opens."
		self.browser.get("http://www.ebay.com")
		link = self.browser.find_element_by_link_text('Sign in')
		link.click()
		self.assertTrue("No results found." not in self.browser.page_source)

if __name__ == "__main__":
	unittest.main(verbosity=2)
