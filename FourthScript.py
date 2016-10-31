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
    
    def test_04_SignInOfAUserWorks(self):
		"Test to make sure that Sign In of a user works fine."
		self.browser.get("http://www.ebay.com")
		link = self.browser.find_element_by_link_text('Sign in')
		link.click()
		emailDiv = self.browser.find_element_by_id("pri_signin")
		emailDivs = emailDiv.find_elements_by_tag_name("div")
		emailSpan = emailDivs[3].find_elements_by_tag_name("span")
		emailInput = emailSpan[1].find_elements_by_tag_name("input")
		emailInput[0].send_keys("vkonduru@kent.edu")
		passwordDiv = self.browser.find_element_by_id("pri_signin")
		passwordDivs = passwordDiv.find_elements_by_tag_name("div")
		passwordSpan = passwordDivs[4].find_elements_by_tag_name("span")
		passwordInput = passwordSpan[1].find_elements_by_tag_name("input")
		passwordInput[0].send_keys("123456789")
		self.browser.find_element_by_id("sgnBt").click()
		self.assertTrue("No results found." not in self.browser.page_source)

if __name__ == "__main__":
	unittest.main(verbosity=2)
