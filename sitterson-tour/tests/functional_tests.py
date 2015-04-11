import unittest
from selenium import webdriver


class HomePageTest(unittest.TestCase):
    def setUp(self):
        self.browser_firefox = webdriver.Firefox()
        self.browser_chrome = webdriver.Chrome()

    def tearDown(self):
        self.browser_firefox.quit()
        self.browser_chrome.quit()

    def test_home_page(self):
        self.browser_firefox.get('http://localhost:8000')
        self.assertIn('Sitterson Tour', self.browser_firefox.title)
        self.browser_chrome.get('http://localhost:8000')
        self.assertIn('Sitterson Tour', self.browser_chrome.title)

if __name__ == '__main__':
    unittest.main()
