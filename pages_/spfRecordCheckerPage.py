from selenium import webdriver
from selenium.webdriver.common.by import By

from pages_.basePage import BasePage


class SPFRecordCheckerPage(BasePage):
    def __init__(self, driver: webdriver.Chrome):
        """
            Initialize the SPFRecordCheckerPage class.
        """
        super().__init__(driver)

        self.__domainNameFieldLocator = (By.CSS_SELECTOR, ".c-form-hard .eas-input")
        self.__checkSPFButtonLocator = (By.CSS_SELECTOR, ".c-form-hard .eas-button")

        self.__spfRecordStatusLocator = (By.XPATH, "(//div[contains(@class, 'spf-lookup-box')]/span[2])[1]")

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

    def get_checked_spf_record_status(self):
        """
            Gets the Checked SPF record status text.
        """
        statusElement = self._find_element(self.__spfRecordStatusLocator)
        statusText = self._get_element_text(statusElement)
        return statusText
