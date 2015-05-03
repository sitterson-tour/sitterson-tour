import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class HomePageTest(unittest.TestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--test-type")
        self.chrome = webdriver.Chrome(chrome_options=chrome_options)
        self.firefox = webdriver.Firefox()

    def tearDown(self):
        self.firefox.quit()
        self.chrome.quit()

    def test_home_page(self):
        self.firefox.get('http://localhost:8000')
        self.assertIn('Sitterson Tour', self.firefox.title)
        self.chrome.get('http://localhost:8000')
        self.assertIn('Sitterson Tour', self.chrome.title)


class AdminTestUsers(unittest.TestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--test-type")
        self.chrome = webdriver.Chrome(chrome_options=chrome_options)
        self.firefox = webdriver.Firefox()

    def tearDown(self):
        self.firefox.quit()
        self.chrome.quit()

    def test_admin_users_firefox(self):
        self.firefox.get('http://localhost:8000/admin/')
        username = self.firefox.find_element_by_id("id_username")
        username.send_keys("demo")
        password = self.firefox.find_element_by_id("id_password")
        password.send_keys("demo")
        self.firefox.find_element_by_xpath('//input[@value="Log in"]').click()
        self.firefox.get('http://localhost:8000/admin/auth/user/add/')
        self.firefox.find_element_by_id("id_username").send_keys("test-firefox")
        self.firefox.find_element_by_id("id_password1").send_keys("test-firefox")
        self.firefox.find_element_by_id("id_password2").send_keys("test-firefox")
        self.firefox.find_element_by_id("user_form").submit()
        self.assertIn("Sitterson Tour Admin", self.firefox.title)

    def test_admin_users_chrome(self):
        self.chrome.get('http://localhost:8000/admin/')
        username = self.chrome.find_element_by_id("id_username")
        username.send_keys("demo")
        password = self.chrome.find_element_by_id("id_password")
        password.send_keys("demo")
        self.chrome.find_element_by_xpath('//input[@value="Log in"]').click()
        self.chrome.get('http://localhost:8000/admin/auth/user/add/')
        self.chrome.find_element_by_id("id_username").send_keys("test-chrome")
        self.chrome.find_element_by_id("id_password1").send_keys("test-chrome")
        self.chrome.find_element_by_id("id_password2").send_keys("test-chrome")
        self.chrome.find_element_by_id("user_form").submit()
        self.assertIn("Sitterson Tour Admin", self.chrome.title)


class AdminTestStops(unittest.TestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--test-type")
        self.chrome = webdriver.Chrome(chrome_options=chrome_options)
        self.firefox = webdriver.Firefox()

    def tearDown(self):
        self.firefox.quit()
        self.chrome.quit()

    def test_admin_stops_firefox(self):
        self.firefox.get('http://localhost:8000/admin/')
        username = self.firefox.find_element_by_id("id_username")
        username.send_keys("demo")
        password = self.firefox.find_element_by_id("id_password")
        password.send_keys("demo")
        self.firefox.find_element_by_xpath('//input[@value="Log in"]').click()
        self.firefox.get('http://localhost:8000/admin/tour/stop/add/')
        self.firefox.find_element_by_id("id_title").send_keys("test-firefox")
        self.firefox.find_element_by_id("id_subtitle").send_keys("test-firefox")
        self.firefox.find_element_by_id("id_slug").send_keys("test-firefox")
        self.firefox.find_element_by_id("stop_form").submit()
        self.firefox.get('http://localhost:8000/stop/test-firefox/')
        self.assertIn("test", self.firefox.title)

    def test_admin_stops_chrome(self):
        self.chrome.get('http://localhost:8000/admin/')
        username = self.chrome.find_element_by_id("id_username")
        username.send_keys("demo")
        password = self.chrome.find_element_by_id("id_password")
        password.send_keys("demo")
        self.chrome.find_element_by_xpath('//input[@value="Log in"]').click()
        self.chrome.get('http://localhost:8000/admin/tour/stop/add/')
        self.chrome.find_element_by_id("id_title").send_keys("test-chrome")
        self.chrome.find_element_by_id("id_subtitle").send_keys("test-chrome")
        self.chrome.find_element_by_id("id_slug").send_keys("test-chrome")
        self.chrome.find_element_by_id("stop_form").submit()
        self.chrome.get('http://localhost:8000/stop/test-chrome/')
        self.assertIn("test", self.chrome.title)


if __name__ == '__main__':
    unittest.main()
