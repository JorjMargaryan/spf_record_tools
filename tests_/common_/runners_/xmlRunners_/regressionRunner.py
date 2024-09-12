from tests_.common_.suites_.testSuites import TestSuites
from common_.reporters_.reporters import Reporters


if __name__ == "__main__":
    testSuites = TestSuites()
    suite = testSuites.get_regression_suite()
    reporter = Reporters()
    runner = reporter.get_xml_test_runner()
    runner.run(suite)
