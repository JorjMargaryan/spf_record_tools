from tests_.baseTest import BaseTest

from pages_.mainPage import MainPage
from pages_.spfRecordGeneratorPage import SPFRecordGeneratorPage
from scripts_.generateData import SPFDataGenerator

from testData_.data import spfRecordGeneratorPageUrl


class DomainNameFieldValidationTests(BaseTest):
    def test_domain_name_field_validation_with_valid_data(self):
        """
            Test Case: Verify the validation of domain name field with valid data.
        """

        # Pre-Condition
        self.driver.get(spfRecordGeneratorPageUrl)
        mainPageObj = MainPage(self.driver)
        mainPageObj.wait_until_the_page_loads()
        mainPageObj.click_to_agree_cookies_button()

        # Act
        generateDataObj = SPFDataGenerator()
        domainName = generateDataObj.generate_domain_name_value()
        spfRecordGeneratorPageObj = SPFRecordGeneratorPage(self.driver)
        spfRecordGeneratorPageObj.fill_domain_name_field(domainName)
        spfRecordGeneratorPageObj.click_to_generate_button()

        # Assertion
        from testData_.data import successStatus
        spfRecordStatus = spfRecordGeneratorPageObj.get_generated_spf_record_status()
        self.assertEqual(spfRecordStatus, successStatus, f"Error: Expected status must be '{successStatus}', but bot '{spfRecordStatus}'")

    def test_domain_name_field_validation_with_invalid_data(self):
        """
            Test Case: Verify that domain name field has checks for incorrect data.
        """
        # Pre-Condition
        self.driver.get(spfRecordGeneratorPageUrl)
        mainPageObj = MainPage(self.driver)
        mainPageObj.wait_until_the_page_loads()
        mainPageObj.click_to_agree_cookies_button()

        # Act
        generateDataObj = SPFDataGenerator()
        domainName = generateDataObj.generate_random_invalid_value("domain")
        spfRecordGeneratorPageObj = SPFRecordGeneratorPage(self.driver)
        spfRecordGeneratorPageObj.fill_domain_name_field(domainName)
        spfRecordGeneratorPageObj.click_to_generate_button()

        # Assertion
        from testData_.data import validationMessageForInvalidData
        actualValidationMessage = spfRecordGeneratorPageObj.get_domain_name_field_validation_message()
        self.assertEqual(actualValidationMessage, validationMessageForInvalidData, f"Error:  Validation Issue - Expected message must be '{validationMessageForInvalidData}', but got '{actualValidationMessage}'")

    def test_domain_name_field_validation_without_data(self):
        """
            Test Case: Verify that domain name field has checks for case without data.
        """
        # Pre-Condition
        self.driver.get(spfRecordGeneratorPageUrl)
        mainPageObj = MainPage(self.driver)
        mainPageObj.wait_until_the_page_loads()
        mainPageObj.click_to_agree_cookies_button()

        # Act
        generateDataObj = SPFDataGenerator()
        domainName = generateDataObj.generate_random_invalid_value("domain")
        spfRecordGeneratorPageObj = SPFRecordGeneratorPage(self.driver)
        spfRecordGeneratorPageObj.fill_domain_name_field(domainName)
        spfRecordGeneratorPageObj.click_to_generate_button()
        spfRecordGeneratorPageObj.clear_domain_name_field()

        # Assertion
        from testData_.data import validationMessageForEmptyData
        actualValidationMessage = spfRecordGeneratorPageObj.get_domain_name_field_validation_message()
        self.assertEqual(actualValidationMessage, validationMessageForEmptyData, f"Error:  Validation Issue - Expected message must be '{validationMessageForEmptyData}', but got '{actualValidationMessage}'")
