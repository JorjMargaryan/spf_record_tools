from selenium import webdriver
from selenium.webdriver.common.by import By

from pages_.basePage import BasePage


class SPFRecordGeneratorPage(BasePage):
    def __init__(self, driver: webdriver.Chrome):
        """
            Initialize the SPFRecordGeneratorPage class.
        """
        super().__init__(driver)

        self.__domainNameFieldLocator = (By.ID, "domain")
        self.__domainNameFieldValidationMessageLocator = (By.CSS_SELECTOR, ".parsley-errors-list")

        self.__useRedirectSwitcherLocator = (By.CLASS_NAME, "eas-toggle-switcher__slider")
        self.__redirectFieldLocator = (By.CSS_SELECTOR, "[data-name='redirect']")

        self.__showMoreButtonLocator = (By.CSS_SELECTOR, ".js-options-show-hide-btn")
        self.__showLessButtonLocator = (By.CSS_SELECTOR, ".show-less-btn")

        self.__includeButtonLocator = (By.CSS_SELECTOR, "[data-option='include']")
        self.__includeFieldLocator = (By.CSS_SELECTOR, "[data-name='include']")
        self.__ipv4ButtonLocator = (By.CSS_SELECTOR, "[data-option='ip4']")
        self.__ipv4FieldLocator = (By.CSS_SELECTOR, "[data-name='ip4']")
        self.__ipv6ButtonLocator = (By.CSS_SELECTOR, "[data-option='ip6']")
        self.__ipv6FieldLocator = (By.CSS_SELECTOR, "[data-name='ip6']")
        self.__aRecordButtonLocator = (By.CSS_SELECTOR, "[data-option='a']")
        self.__aRecordFieldLocator = (By.CSS_SELECTOR, "[data-name='a']")
        self.__mxRecordButtonLocator = (By.CSS_SELECTOR, "[data-option='mx']")
        self.__mxRecordFieldLocator = (By.CSS_SELECTOR, "[data-name='mx']")
        self.__existsButtonLocator = (By.CSS_SELECTOR, "[data-option='exists']")
        self.__existsFieldLocator = (By.CSS_SELECTOR, "[data-name='exists']")
        self.__deleteOptionButtonLocator = (By.CSS_SELECTOR, ".js-delete-option-btn")

        self.__failurePolicyDropdownLocator = (By.ID, "dropdownMenuButton")
        self.__failurePolicyDropdownOpenedStateLocator = (By.CSS_SELECTOR, ".eas-select .show")
        self.__noneValueLocator = (By.CSS_SELECTOR, "[data-value='None']")
        self.__failValueLocator = (By.CSS_SELECTOR, "[data-value='Fail']")
        self.__softFailValueLocator = (By.CSS_SELECTOR, "[data-value='SoftFail']")
        self.__neutralValueLocator = (By.CSS_SELECTOR, "[data-value='Neutral']")

        self.__generateButtonLocator = (By.CSS_SELECTOR, ".js-spf-generator-submit-form-btn")

        self.__spfRecordStatusLocator = (By.XPATH, "(//div[contains(@class, 'spf-lookup-box')]/span[2])[1]")
        self.__generatedSpfRecordHostTextLocator = (By.XPATH, "//span[@id='spf-host']")
        self.__generatedSpfRecordHostCopyButtonLocator = (By.CSS_SELECTOR, "[data-clipboard-target='#spf-host']")
        self.__generatedSpfRecordTypeTextLocator = (By.ID, "spf-type")
        self.__generatedSpfRecordValueTextLocator = (By.XPATH, "//span[@id='generated-spf-record']")
        self.__generatedSpfRecordValueCopyButtonLocator = (By.CSS_SELECTOR, "[data-clipboard-target='#generated-spf-record']")

    def __clear_provided_field(self, fieldLocator):
        """
            Clears the provided field by selecting all text and pressing backspace.
        """
        from selenium.webdriver.common.keys import Keys

        fieldElement = self._find_element(fieldLocator)
        fieldElement.click()  # Click on the field to focus
        fieldElement.send_keys(Keys.CONTROL + "a")  # Select all text (Cmd + A on Mac)
        fieldElement.send_keys(Keys.BACKSPACE)  # Press backspace to delete the text

        # Alternatively, can be used the DELETE key
        # fieldElement.send_keys(Keys.DELETE)  # Press delete to clear the text

    def __fill_provided_field(self, fieldLocator, value):
        """
            Fills the provided field with provided value.
        """
        fieldElement = self._find_element(fieldLocator)
        self._fill_field(fieldElement, value)

    def __click_to_provided_element(self, elementLocator):
        """
            Clicks on the element identified by the provided locator.
        """
        element = self._find_element(elementLocator)
        self._click_to_element(element)

    def fill_domain_name_field(self, domainName):
        """
            Fills the domain name field with provided domain name.
        """
        self.__fill_provided_field(self.__domainNameFieldLocator, domainName)

    def clear_domain_name_field(self):
        """
            Clears the domain name field.
        """
        self.__clear_provided_field(self.__domainNameFieldLocator)

    def click_to_show_more_button(self):
        """
            Clicks on the Show More button from the  'Choose Source values' area.
        """
        self.__click_to_provided_element(self.__showMoreButtonLocator)

    def click_to_show_less_button(self):
        """
            Clicks on the Show Less button from the  'Choose Source values' area.
        """
        self.__click_to_provided_element(self.__showLessButtonLocator)

    def add_include_option(self):
        """
             Adds Include option by clicking on the Include button from the 'Choose Source values' area.
        """
        self.__click_to_provided_element(self.__includeButtonLocator)

    def fill_include_field(self, includeValue):
        """
            Fills an include field with provided value.
        """
        self.__fill_provided_field(self.__includeFieldLocator, includeValue)

    def add_ipv4_option(self):
        """
             Adds Ipv4 option by clicking on the Ipv4 button from the 'Choose Source values' area.
        """
        self.__click_to_provided_element(self.__ipv4ButtonLocator)

    def fill_ipv4_field(self, ipValue):
        """
            Fills an Ipv4 field with provided value.
        """
        self.__fill_provided_field(self.__ipv4FieldLocator, ipValue)

    def add_ipv6_option(self):
        """
             Adds Ipv6 option by clicking on the Ipv6 button from the 'Choose Source values' area.
        """
        self.__click_to_provided_element(self.__ipv6ButtonLocator)

    def fill_ipv6_field(self, ipValue):
        """
            Fills an Ipv6 field with provided value.
        """
        self.__fill_provided_field(self.__ipv6FieldLocator, ipValue)

    def add_a_record_option(self):
        """
             Adds 'A record' option by clicking on the 'A record' button from the 'Choose Source values' area.
        """
        self.__click_to_provided_element(self.__aRecordButtonLocator)

    def fill_a_record_field(self, aRecordValue):
        """
            Fills an A Record field with provided value.
        """
        self.__fill_provided_field(self.__aRecordFieldLocator, aRecordValue)

    def add_mx_record_option(self):
        """
             Adds 'MX record' option by clicking on the 'MX record' button from the 'Choose Source values' area.
        """
        self.__click_to_provided_element(self.__mxRecordButtonLocator)

    def fill_mx_record_field(self, mxRecordValue):
        """
            Fills the Mx Record field with provided value.
        """
        self.__fill_provided_field(self.__mxRecordFieldLocator, mxRecordValue)

    def add_exists_option(self):
        """
             Adds 'Exists' option by clicking on the 'Exists' button from the 'Choose Source values' area.
        """
        self.__click_to_provided_element(self.__existsButtonLocator)

    def fill_exists_field(self, existsValue):
        """
            Fills an Exists field with provided value.
        """
        self.__fill_provided_field(self.__existsFieldLocator, existsValue)

    def click_to_failure_policy_dropdown(self):
        """
            Clicks on the "Failure Policy" dropdown.
        """
        self.__click_to_provided_element(self.__failurePolicyDropdownLocator)

    def select_value_none_from_dropdown(self):
        """
            Clicks on the value "None" from the Failure Policy dropdown.
        """
        self.__click_to_provided_element(self.__noneValueLocator)

    def select_value_fail_from_dropdown(self):
        """
            Clicks on the value "Fail" from the Failure Policy dropdown.
        """
        self.__click_to_provided_element(self.__failValueLocator)

    def select_value_soft_fail_from_dropdown(self):
        """
            Clicks on the value "SoftFail" from the Failure Policy dropdown.
        """
        self.__click_to_provided_element(self.__softFailValueLocator)

    def select_value_neutral_from_dropdown(self):
        """
            Clicks on the value "Neutral" from the Failure Policy dropdown.
        """
        self.__click_to_provided_element(self.__neutralValueLocator)

    def click_to_generate_button(self):
        """
            Clicks on the "Generate" button.
        """
        self.__click_to_provided_element(self.__generateButtonLocator)

    def get_generated_spf_record_status(self):
        """
            Gets the generated SPF record status text.
        """
        statusElement = self._find_element(self.__spfRecordStatusLocator)
        statusText = self._get_element_text(statusElement)

        return statusText

    def get_generated_spf_record_data(self):
        """
            Gets the generated SPF record data(host, type, spf value).
        """
        hostValueElement = self._find_element(self.__generatedSpfRecordHostTextLocator)
        hostValue = self._get_element_text(hostValueElement)
        spfRecordTypeElement = self._find_element(self.__generatedSpfRecordTypeTextLocator)
        spfRecordType = self._get_element_text(spfRecordTypeElement)
        spfRecordValueElement = self._find_element(self.__generatedSpfRecordValueTextLocator)
        spfRecordValue = self._get_element_text(spfRecordValueElement)

        return hostValue, spfRecordType, spfRecordValue

    def get_domain_name_field_validation_message(self):
        """
            Gets the domain name field validation message.
        """
        messageElement = self._find_element(self.__domainNameFieldValidationMessageLocator)
        messageText = self._get_element_text(messageElement)
        return messageText
