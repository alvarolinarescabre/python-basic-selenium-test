iimport unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


driver = webdriver.Remote(
   command_executor='http://<selenium-ip>:4444/wd/hub',
   desired_capabilities={'browserName': 'chrome', 'javascriptEnabled': True,})

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu') 

class SeleniumTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(options=options)

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org")
        assert "Python" in driver.title
        elem = driver.find_element_by_name("q")
        elem.clear()
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()

