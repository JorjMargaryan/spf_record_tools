from tests_.baseTest import BaseTest

from pages_.mainPage import MainPage
from pages_.spfRecordValidatorPage import SPFRecordValidatorPage
from scripts_.generateData import SPFDataGenerator

from testData_.data import spfRecordValidatorPageUrl
import time


class ValidateSPFRecordTests(BaseTest):
    def setUp(self):
        super().setUp()

        # Pre-Condition
        self.driver.get(spfRecordValidatorPageUrl)
        mainPageObj = MainPage(self.driver)
        mainPageObj.wait_until_the_page_loads()
        mainPageObj.click_to_agree_cookies_button()

        self.spfRecordValidatorPageObj = SPFRecordValidatorPage(self.driver)
        self.generateDataObj = SPFDataGenerator()

    def test_validate_spf_record_with_valid_data(self):
        """
            Test Case: Verify the functionality of validating SPF record with valid data.
        """
        from testData_.data import successStatus, validateSpfRecordAcceptableTime
        # Act
        domainName = self.generateDataObj.generate_domain_name_value()
        self.spfRecordValidatorPageObj.fill_domain_name_field(domainName)

        validSpfRecord = self.generateDataObj.generate_spf_record(include=True, ipv4=True, ipv6=True, aRecord=True, mxRecord=True, exists=True, failurePolicy="Fail")
        self.spfRecordValidatorPageObj.fill_raw_record_field(validSpfRecord)

        # Measure the time taken to validate an SPF record
        startTime = time.time()
        self.spfRecordValidatorPageObj.click_to_validate_spf_record_button()

        # Assertion
        spfRecordStatus = self.spfRecordValidatorPageObj.get_validated_spf_record_status()

        endTime = time.time()
        responseTime = endTime - startTime
        # Assertion for response time
        self.assertLess(responseTime, validateSpfRecordAcceptableTime, f"Error: Response time is {responseTime} seconds, which exceeds the acceptable limit of {validateSpfRecordAcceptableTime} seconds")

        self.assertEqual(spfRecordStatus, successStatus, f"Error: Expected status must be '{successStatus}', but got '{spfRecordStatus}'")

    def test_validate_spf_record_with_invalid_data(self):
        """
            Test Case: Verify the functionality of validating SPF record with invalid data.
        """
        # Act
        domainName = self.generateDataObj.generate_domain_name_without_spf()
        self.spfRecordValidatorPageObj.fill_domain_name_field(domainName)

        invalidSpfRecord = self.generateDataObj.generate_spf_record(valid=False, include=True, ipv4=True, ipv6=True, aRecord=True, mxRecord=True, exists=True, failurePolicy="None")
        self.spfRecordValidatorPageObj.fill_raw_record_field(invalidSpfRecord)

        # Measure the time taken to validate an SPF record
        startTime = time.time()
        self.spfRecordValidatorPageObj.click_to_validate_spf_record_button()

        # Assertion
        from testData_.data import validateSpfRecordAcceptableTime, failStatus
        spfRecordStatus = self.spfRecordValidatorPageObj.get_validated_spf_record_status()

        endTime = time.time()
        responseTime = endTime - startTime
        # Assertion for response time
        self.assertLess(responseTime, validateSpfRecordAcceptableTime, f"Error: Response time is {responseTime} seconds, which exceeds the acceptable limit of {validateSpfRecordAcceptableTime} seconds")

        self.assertEqual(spfRecordStatus, failStatus, f"Error: Expected status must be '{failStatus}', but got '{spfRecordStatus}'")
        # TODO Add other assertions for error and warning messages
