from selenium import webdriver
from selenium.webdriver.common.by import By

from pages_.basePage import BasePage


class MainPage(BasePage):
    def __init__(self, driver: webdriver.Chrome):
        """
            Initialize the MainPage class.
        """
        super().__init__(driver)

        self.__toolsButtonActiveStateLocator = (By.CSS_SELECTOR, ".c-active-tools.active")
        self.__agreeCookiesButton = (By.CLASS_NAME, "cookie-consent-button")

    def wait_until_the_page_loads(self):
        """
            Checks if the Tools button on the navigation bar is active, simulating waiting for the page to load.
        """
        self._element_should_be_present(self.__toolsButtonActiveStateLocator, 15)

    def click_to_agree_cookies_button(self):
        """
            Clicks the "Agree" button to confirm the use of cookies.
        """
        agreeButtonElement = self._find_element(self.__agreeCookiesButton)
        self._click_to_element(agreeButtonElement)
