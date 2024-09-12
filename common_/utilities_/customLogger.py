from pathlib import Path
import logging
import os
from datetime import datetime


def get_root_directory():
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
        logger("ERROR", f"{MessageCodes[FILE_NOT_FOUND]} - {str(e)}")
        exit(FILE_NOT_FOUND)
    except Exception as e:
        logger("ERROR", f"{MessageCodes[UNEXPECTED_BEHAVIOR]} - {str(e)}")
        exit(UNEXPECTED_BEHAVIOR)


def logger(level, message, fileName=os.path.join(get_root_directory(), 'logs_', f'log_{datetime.now().strftime("%d_%m_%Y_%H-%M-%S")}.log')):
    """
        Log messages at different log levels (INFO, DEBUG, WARNING, ERROR, CRITICAL) with exception handling.

        This function configures a logger to write log messages to a specified file. It supports multiple log levels:
        - INFO: Informational messages
        - DEBUG: Debugging messages
        - WARNING: Warnings
        - ERROR: Errors
        - CRITICAL: Critical errors
    """
    from exitCodes import MessageCodes, LOGGING_ERROR
    try:
        logging.basicConfig(level=logging.INFO, filename=fileName, filemode="a",
                            format="%(asctime)-12s %(levelname)s %(message)s",
                            datefmt="%d-%m-%Y %H:%M:%S")

        if level == "INFO":
            logging.info(message)
        elif level == "DEBUG":
            logging.debug(message)
        elif level == "WARNING":
            logging.warning(message)
        elif level == "ERROR":
            logging.error(message)
        elif level == "CRITICAL":
            logging.critical(message)
    except Exception as e:
        logger("ERROR", f"{MessageCodes[LOGGING_ERROR]} - {str(e)}")
        exit(LOGGING_ERROR)
