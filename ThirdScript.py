from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import unittest

class Test_PythonOrg(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Safari()

	def tearDown(self):
		sleep(4)
		self.browser.close()
		self.browser = None
    
    def test_03_RegisterAUserWorks(self):
		self.browser.get("http://www.ebay.com")
		link = self.browser.find_element_by_link_text('register')
		link.click()
		email = self.browser.find_element_by_id("email")
		reEmail = self.browser.find_element_by_id("remail")
		password = self.browser.find_element_by_id("PASSWORD")
		firstName = self.browser.find_element_by_id("firstname")
		lastName = self.browser.find_element_by_id("lastname")
		mobile = self.browser.find_element_by_id("phoneFlagComp1")
		email.send_keys("abc.com")
		reEmail.send_keys("abc.com")
		password.send_keys("123456789")
		firstName.send_keys("First")
		lastName.send_keys("Last")
		mobile.send_keys("123456789")
		self.browser.find_element_by_id("sbtBtn").click()
		self.assertTrue("No results found." not in self.browser.page_source)
    
if __name__ == "__main__":
	unittest.main(verbosity=2)
