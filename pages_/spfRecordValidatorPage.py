from selenium import webdriver
from selenium.webdriver.common.by import By

from basePage import BasePage


class SPFRecordValidatorPage(BasePage):
    def __init__(self, driver: webdriver.Chrome):
        """
            Initialize the SPFRecordValidatorPage class.
        """
        super().__init__(driver)

        self.__domainNameFieldLocator = (By.ID, "domain")
        self.__rawRecordFieldLocator = (By.ID, "raw_record")
        self.__validateSPFRecordButtonLocator = (By.CSS_SELECTOR, ".c-form-hard .eas-button")

    def fill_domain_name_field(self, domainName):
        """
            Fills the domain name field with provided domain name.
        """
        domainNameFieldElement = self._find_element(self.__domainNameFieldLocator)
        self._fill_field(domainNameFieldElement, domainName)

    def fill_raw_record_field(self, spfRecordText):
        """
            Fills the Raw Record field with provided SPF record text.
        """
        rawRecordFieldElement = self._find_element(self.__rawRecordFieldLocator)
        self._fill_field(rawRecordFieldElement, spfRecordText)

    def click_to_validate_spf_record_button(self):
        """
            Clicks on the "Validate SPF Record" button.
        """
        validateSPFRecordButtonElement = self._find_element(self.__validateSPFRecordButtonLocator)
        self._click_to_element(validateSPFRecordButtonElement)
