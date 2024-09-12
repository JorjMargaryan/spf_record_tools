import unittest

from tests_.testCases_.spfRecordGeneratorTests_.generateSpfRecordTests import GenerateSPFRecordTests
from tests_.testCases_.spfRecordGeneratorTests_.domainNameFieldValidationTests import DomainNameFieldValidationTests


class TestSuites:
    """
        This class provides methods to create test suites for various testing scenarios, allowing for organized and
        purpose-driven test case grouping.
    """
    def get_regression_suite(self):
        suite = unittest.TestSuite()
        suite.addTest(GenerateSPFRecordTests("test_generate_spf_record_with_all_fields_with_valid_data"))
        suite.addTest(GenerateSPFRecordTests("test_generate_spf_record_with_invalid_data"))
        suite.addTest(DomainNameFieldValidationTests("test_domain_name_field_validation_with_valid_data"))
        suite.addTest(DomainNameFieldValidationTests("test_domain_name_field_validation_with_invalid_data"))
        suite.addTest(DomainNameFieldValidationTests("test_domain_name_field_validation_without_data"))

        return suite

    def get_smoke_suite(self):
        pass

    def get_performance_suite(self):
        pass

    def get_random_suite(self):
        pass
