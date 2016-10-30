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

	def test_00_SearchBoxWorks(self):
		"Test to make sure that the search box works fine."
		self.browser.get("http://www.ebay.com")
		search_entry = self.browser.find_element_by_name("_nkw")
		search_entry.clear()
		search_entry.send_keys("iphone7")
		search_entry.send_keys(Keys.RETURN)
		self.assertTrue("No results found." not in self.browser.page_source)

if __name__ == "__main__":
	unittest.main(verbosity=2)
