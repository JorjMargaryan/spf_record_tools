from tests_.baseTest import BaseTest

from pages_.mainPage import MainPage
from pages_.spfRecordGeneratorPage import SPFRecordGeneratorPage
from scripts_.generateData import SPFDataGenerator

from testData_.data import spfRecordGeneratorPageUrl
import time


class GenerateSPFRecordTests(BaseTest):
    def setUp(self):
        super().setUp()

        # Pre-Condition
        self.driver.get(spfRecordGeneratorPageUrl)
        mainPageObj = MainPage(self.driver)
        mainPageObj.wait_until_the_page_loads()
        mainPageObj.click_to_agree_cookies_button()

        self.spfRecordGeneratorObj = SPFRecordGeneratorPage(self.driver)
        self.spfRecordGeneratorObj.click_to_show_more_button()
        self.spfRecordGeneratorObj.add_ipv4_option()
        self.spfRecordGeneratorObj.add_ipv6_option()
        self.spfRecordGeneratorObj.add_a_record_option()
        self.spfRecordGeneratorObj.add_mx_record_option()
        self.spfRecordGeneratorObj.add_exists_option()
        self.generateDataObj = SPFDataGenerator()

    def test_generate_spf_record_with_all_fields_with_valid_data(self):
        """
            Test Case: Verify the functionality of generating SPF record with all fields with valid data.
        """
        from testData_.data import successStatus, spfRecordVersion, spfRecordType, softFailValue, generateSpfResponseAcceptableTime
        # Act
        domainName = self.generateDataObj.generate_domain_name_value()
        self.spfRecordGeneratorObj.fill_domain_name_field(domainName)
        includeValue = self.generateDataObj.generate_include_value()
        self.spfRecordGeneratorObj.fill_include_field(includeValue)
        ipv4Value = self.generateDataObj.generate_ipv4_value()
        self.spfRecordGeneratorObj.fill_ipv4_field(ipv4Value)
        ipv6Value = self.generateDataObj.generate_ipv6_value()
        self.spfRecordGeneratorObj.fill_ipv6_field(ipv6Value)
        aRecordValue = self.generateDataObj.generate_a_record_value()
        self.spfRecordGeneratorObj.fill_a_record_field(aRecordValue)
        mxRecordValue = self.generateDataObj.generate_mx_record_value()
        self.spfRecordGeneratorObj.fill_mx_record_field(mxRecordValue)
        existsValue = self.generateDataObj.generate_exists_value()
        self.spfRecordGeneratorObj.fill_exists_field(existsValue)

        self.spfRecordGeneratorObj.click_to_failure_policy_dropdown()
        self.spfRecordGeneratorObj.select_value_soft_fail_from_dropdown()

        # Measure the time taken to generate an SPF record
        startTime = time.time()
        self.spfRecordGeneratorObj.click_to_generate_button()

        # Assertion
        spfRecordStatus = self.spfRecordGeneratorObj.get_generated_spf_record_status()

        endTime = time.time()
        responseTime = endTime - startTime
        # Assertion for response time
        self.assertLess(responseTime, generateSpfResponseAcceptableTime, f"Error: Response time is {responseTime} seconds, which exceeds the acceptable limit of {generateSpfResponseAcceptableTime} seconds")

        self.assertEqual(spfRecordStatus, successStatus, f"Error: Expected status must be '{successStatus}', but got '{spfRecordStatus}'")
        hostValue, typeValue, spfRecordValue = self.spfRecordGeneratorObj.get_generated_spf_record_data()
        self.assertEqual(domainName, hostValue, f"Error: Expected host must be '{domainName}', but got '{hostValue}'")
        self.assertEqual(typeValue, spfRecordType, f"Error:Expected type must be '{spfRecordType}', but got '{typeValue}'")
        self.assertIn(spfRecordVersion, spfRecordValue, f"Error: SPF version '{spfRecordVersion}'not found in SPF record")
        self.assertIn(includeValue, spfRecordValue, f"Error: Include value '{includeValue}' not found in SPF record")
        self.assertIn(ipv4Value, spfRecordValue, f"Error: IPv4 value '{ipv4Value}' not found in SPF record")
        self.assertIn(ipv6Value, spfRecordValue, f"Error: IPv6 value '{ipv6Value}' not found in SPF record")
        self.assertIn(aRecordValue, spfRecordValue, f"Error: A record value '{aRecordValue}' not found in SPF record")
        self.assertIn(mxRecordValue, spfRecordValue, f"Error: MX record value '{mxRecordValue}' not found in SPF record")
        self.assertIn(existsValue, spfRecordValue, f"Exists value '{existsValue}' not found in SPF record")
        self.assertIn(softFailValue, spfRecordValue, "Error: SoftFail policy not found in SPF record")

    def test_generate_spf_record_with_invalid_data(self):
        """
            Test Case: Verify that generate SPF record functionality has checks for incorrect data.
        """
        # Act
        domainName = self.generateDataObj.generate_domain_name_value()
        self.spfRecordGeneratorObj.fill_domain_name_field(domainName)
        includeValue = self.generateDataObj.generate_random_invalid_value("include")
        self.spfRecordGeneratorObj.fill_include_field(includeValue)
        ipv4Value = self.generateDataObj.generate_random_invalid_value("ipv4")
        self.spfRecordGeneratorObj.fill_ipv4_field(ipv4Value)
        ipv6Value = self.generateDataObj.generate_random_invalid_value("ipv6")
        self.spfRecordGeneratorObj.fill_ipv6_field(ipv6Value)
        aRecordValue = self.generateDataObj.generate_random_invalid_value("aRecord")
        self.spfRecordGeneratorObj.fill_a_record_field(aRecordValue)
        mxRecordValue = self.generateDataObj.generate_random_invalid_value("mxRecord")
        self.spfRecordGeneratorObj.fill_mx_record_field(mxRecordValue)
        existsValue = self.generateDataObj.generate_random_invalid_value("exists")
        self.spfRecordGeneratorObj.fill_exists_field(existsValue)

        self.spfRecordGeneratorObj.click_to_failure_policy_dropdown()
        self.spfRecordGeneratorObj.select_value_none_from_dropdown()

        # Measure the time taken to generate an SPF record
        startTime = time.time()
        self.spfRecordGeneratorObj.click_to_generate_button()

        # Assertion
        from testData_.data import generateSpfResponseAcceptableTime, failStatus
        spfRecordStatus = self.spfRecordGeneratorObj.get_generated_spf_record_status()

        endTime = time.time()
        responseTime = endTime - startTime
        # Assertion for response time
        self.assertLess(responseTime, generateSpfResponseAcceptableTime, f"Error: Response time is {responseTime} seconds, which exceeds the acceptable limit of {generateSpfResponseAcceptableTime} seconds")

        self.assertEqual(spfRecordStatus, failStatus, f"Error: Expected status must be '{failStatus}', but got '{spfRecordStatus}'")
        # TODO Add more assertions for error and warning messages
