import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.events import EventFiringWebDriver

from common_.utilities_.customListener import CustomListener


class BaseTest(unittest.TestCase):
    """
        This class serves as the base for Selenium test cases, providing common setup and tear down procedures.
    """
    def setUp(self):
        """
                # Options for run browser in headless mode

        from selenium.webdriver.chrome.options import Options
        chromeOptions = Options()
        chromeOptions.add_argument("--headless")
        chromeOptions.add_argument("--no-sandbox")  # Disable sandbox mode
        self.simpleDriver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chromeOptions)
        """

        self.simpleDriver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver = EventFiringWebDriver(self.simpleDriver, CustomListener(self.simpleDriver))
        self.driver.delete_all_cookies()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.close()
