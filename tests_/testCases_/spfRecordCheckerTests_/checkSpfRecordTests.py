from tests_.baseTest import BaseTest

from pages_.mainPage import MainPage
from pages_.spfRecordCheckerPage import SPFRecordCheckerPage
from scripts_.generateData import SPFDataGenerator

from testData_.data import spfRecordCheckerPageUrl
import time


class CheckSPFRecordTests(BaseTest):
    def setUp(self):
        super().setUp()

        # Pre-Condition
        self.driver.get(spfRecordCheckerPageUrl)
        mainPageObj = MainPage(self.driver)
        mainPageObj.wait_until_the_page_loads()
        mainPageObj.click_to_agree_cookies_button()

        self.spfRecordCheckerObj = SPFRecordCheckerPage(self.driver)
        self.generateDataObj = SPFDataGenerator()

    def test_check_spf_record_with_valid_data(self):
        """
            Test Case: Verify the functionality of checking SPF record with valid data.
        """
        from testData_.data import successStatus, checkSpfResponseAcceptableTime
        # Act
        domainName = self.generateDataObj.generate_include_value()
        self.spfRecordCheckerObj.fill_domain_name_field(domainName)

        # Measure the time taken to generate an SPF record
        startTime = time.time()
        self.spfRecordCheckerObj.click_to_check_spf_button()

        # Assertion
        spfRecordStatus = self.spfRecordCheckerObj.get_checked_spf_record_status()

        endTime = time.time()
        responseTime = endTime - startTime
        # Assertion for response time
        self.assertLess(responseTime, checkSpfResponseAcceptableTime, f"Error: Response time is {responseTime} seconds, which exceeds the acceptable limit of {checkSpfResponseAcceptableTime} seconds")

        self.assertEqual(spfRecordStatus, successStatus, f"Error: Expected status must be '{successStatus}', but got '{spfRecordStatus}'")

    def test_check_spf_record_with_invalid_data(self):
        """
            Test Case: Verify the functionality of checking SPF record with invalid data.
        """
        # Act
        domainName = self.generateDataObj.generate_domain_name_without_spf()
        self.spfRecordCheckerObj.fill_domain_name_field(domainName)

        # Measure the time taken to generate an SPF record
        startTime = time.time()
        self.spfRecordCheckerObj.click_to_check_spf_button()

        # Assertion
        from testData_.data import checkSpfResponseAcceptableTime, noRecordStatus
        spfRecordStatus = self.spfRecordCheckerObj.get_checked_spf_record_status()

        endTime = time.time()
        responseTime = endTime - startTime
        # Assertion for response time
        self.assertLess(responseTime, checkSpfResponseAcceptableTime, f"Error: Response time is {responseTime} seconds, which exceeds the acceptable limit of {checkSpfResponseAcceptableTime} seconds")

        self.assertEqual(spfRecordStatus, noRecordStatus, f"Error: Expected status must be '{noRecordStatus}', but got '{spfRecordStatus}'")
        # TODO Add another assertions for error messages
