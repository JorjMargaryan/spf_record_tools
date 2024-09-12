from selenium import webdriver
from selenium.webdriver.common.by import By

from basePage import BasePage


class SPFRecordCheckerPage(BasePage):
    def __init__(self, driver: webdriver.Chrome):
        """
            Initialize the SPFRecordCheckerPage class.
        """
        super().__init__(driver)

        self.__domainNameFieldLocator = (By.CSS_SELECTOR, ".c-form-hard .eas-input")
        self.__checkSPFButtonLocator = (By.CSS_SELECTOR, ".c-form-hard .eas-button")

    def fill_domain_name_field(self, domainName):
        """
            Fills the domain name field with provided domain name.
        """
        domainNameFieldElement = self._find_element(self.__domainNameFieldLocator)
        self._fill_field(domainNameFieldElement, domainName)

    def click_to_check_spf_button(self):
        """
            Clicks on the "Check SPF" button.
        """
        checkSPFButtonElement = self._find_element(self.__checkSPFButtonLocator)
        self._click_to_element(checkSPFButtonElement)
