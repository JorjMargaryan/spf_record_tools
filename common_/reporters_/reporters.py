import os
from pathlib import Path
import datetime

from common_.reporters_.sources_.htmlTestRunner import HTMLTestRunner
from xmlrunner import XMLTestRunner
from common_.utilities_ import customLogger


class Reporters:
    def __get_root_directory(self):
        """
            Gets the root directory path for the project.
        """
        from exitCodes import MessageCodes, FILE_NOT_FOUND, UNEXPECTED_BEHAVIOR
        try:
            projectName = "spf_record_tools"
            currentPath = Path(__file__)
            projectRootPath = (str(currentPath).split(projectName))[0] + projectName
            return projectRootPath
        except FileNotFoundError as e:
            customLogger.logger("ERROR", f"{MessageCodes[FILE_NOT_FOUND]} - {str(e)}")
            exit(FILE_NOT_FOUND)
        except Exception as e:
            customLogger.logger("ERROR", f"{MessageCodes[UNEXPECTED_BEHAVIOR]} - {str(e)}")
            exit(UNEXPECTED_BEHAVIOR)

    def __generate_report_file_name(self, fileFormat):
        """
            This method generates a report file name in the format 'report_DD-MM-YYYY_HH-MM-SS.html' or 'report_DD-MM-YYYY_HH-MM-SS.xml' based on
            the current date and time. The formatted date and time are obtained using Python's datetime module.
        """
        from exitCodes import MessageCodes, FILE_NAME_GENERATION_ERROR
        try:
            current_datetime = datetime.datetime.now()
            formatted_datetime = current_datetime.strftime('%d-%m-%Y_%H-%M-%S')
            reportFileName = f"report_{formatted_datetime}.{fileFormat}"
            return reportFileName
        except Exception as e:
            customLogger.logger("ERROR", f"{MessageCodes[FILE_NAME_GENERATION_ERROR]} - {str(e)}")
            exit(FILE_NAME_GENERATION_ERROR)

    def get_html_test_runner(self, title='Test Report', description="Test description"):
        """
            This method creates an HTMLTestRunner instance with the specified title and description. It also sets the
            output file for the test report created by using the current project's root directory and a generated report file name.
        """
        from exitCodes import MessageCodes, REPORT_CREATION_ERROR
        try:
            # Open the HTML report file within the directory for writing
            rootDirectory = self.__get_root_directory()
            reportsDirectory = os.path.join(rootDirectory, "reports_")
            reportFileName = self.__generate_report_file_name("html")
            # Create a report file and place it in the reports_ directory.(The format-rootDirectory/reports_/reportFileName )
            reportFile = open(os.path.join(reportsDirectory, reportFileName), "wb")
            runner = HTMLTestRunner(
                stream=reportFile,
                title=title,
                description=description
            )
            return runner
        except Exception as e:
            customLogger.logger("ERROR", f"{MessageCodes[REPORT_CREATION_ERROR]} - {str(e)}")
            exit(REPORT_CREATION_ERROR)

    def get_xml_test_runner(self):
        """
            This method creates an XMLTestRunner instance with the specified output file for the test report created by using
            the current project's root directory and a generated report file name.
        """
        from exitCodes import MessageCodes, REPORT_CREATION_ERROR
        try:
            # Open the HTML report file within the directory for writing
            rootDirectory = self.__get_root_directory()
            reportsDirectory = os.path.join(rootDirectory, "reports_")
            reportFileName = self.__generate_report_file_name("xml")
            # Create a report file and place it in the reports_ directory.(The format-rootDirectory/reports_/reportFileName )
            reportFile = open(os.path.join(reportsDirectory, reportFileName), "wb")
            runner = XMLTestRunner(output=reportFile)
            return runner
        except Exception as e:
            customLogger.logger("ERROR", f"{MessageCodes[REPORT_CREATION_ERROR]} - {str(e)}")
            exit(REPORT_CREATION_ERROR)
