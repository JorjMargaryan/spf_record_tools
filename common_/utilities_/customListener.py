from selenium.webdriver.support.events import AbstractEventListener
from common_.utilities_ import customLogger


class CustomListener(AbstractEventListener):
    def __init__(self, driver):
        """
            This constructor sets up the CustomListener for monitoring WebDriver events.
    
            Attributes:
                driver (webdriver.Chrome): The WebDriver instance to which this listener is attached.
                browserName (str): The name of the browser being used (e.g., 'Chrome', 'Firefox').
                browserVersion (str): The version of the browser being used.
                platformName (str): The name of the platform on which the browser is running (e.g., 'Windows', 'Linux').
        """
        self.driver = driver
        self.browserName = driver.capabilities['browserName']
        self.browserVersion = driver.capabilities['browserVersion']
        self.platformName = driver.capabilities['platformName']

    # def before_navigate_to(self, url, driver):
    #     """
    #         Called before navigating to a new URL.
    #
    #         Args:
    #             url (str): The URL to navigate to.
    #             driver (webdriver.Chrome): The WebDriver instance.
    #     """
    #     customLogger.logger("INFO", f"Preparing to navigate to: {url} using {self.browserName} driver (Version {self.browserVersion}) on {self.platformName}")

    def after_navigate_to(self, url, driver):
        """
            Called after successfully navigating to a new URL.

            Args:
                url (str): The URL that was navigated to.
                driver (webdriver.Chrome): The WebDriver instance.
        """
        customLogger.logger("INFO", f"Successfully navigated to: {url} using {self.browserName} driver (Version {self.browserVersion}) on {self.platformName}")

    # def before_navigate_back(self, driver):
    #     """
    #         Called before navigating back to the previous page.
    #
    #         Args:
    #             driver (webdriver.Chrome): The WebDriver instance.
    #     """
    #     customLogger.logger("INFO", f"Preparing to navigate back from: {driver.current_url} in {self.browserName} driver (Version {self.browserVersion}) on {self.platformName}")

    def after_navigate_back(self, driver):
        """
            Called after successfully navigating back to the previous page.

            Args:
                driver (webdriver.Chrome): The WebDriver instance.
        """
        customLogger.logger("INFO", f"Successfully navigated back to: {driver.current_url} in {self.browserName} driver (Version {self.browserVersion}) on {self.platformName}")

    # def before_navigate_forward(self, driver):
    #     """
    #         Called before navigating forward to a page.
    #
    #         Args:
    #             driver (webdriver.Chrome): The WebDriver instance.
    #     """
    #     customLogger.logger("INFO", f"Preparing to navigate forward from: {driver.current_url} in {self.browserName} driver (Version {self.browserVersion}) on {self.platformName}")

    def after_navigate_forward(self, driver):
        """
            Called after successfully navigating forward to a page.

            Args:
                driver (webdriver.Chrome): The WebDriver instance.
        """
        customLogger.logger("INFO", f"Successfully navigated forward to: {driver.current_url} in {self.browserName} driver (Version {self.browserVersion}) on {self.platformName}")

    # def before_find(self, by, value, driver):
    #     """
    #         Called before attempting to find an element by a specific locator.
    #
    #         Args:
    #             by: The locator strategy used to find the element.
    #             value: The value of the locator.
    #             driver (webdriver.Chrome): The WebDriver instance.
    #     """
    #     customLogger.logger("INFO", f"Preparing to find an element with the locator By: {by}, Value: {value} using {self.browserName} driver (Version {self.browserVersion}) on {self.platformName}")

    def after_find(self, by, value, driver):
        """
            Called after successfully finding an element by a specific locator.

            Args:
                by: The locator strategy used to find the element.
                value: The value of the locator.
                driver (webdriver.Chrome): The WebDriver instance.
        """
        customLogger.logger("INFO", f"An element was successfully found using the locator By: {by}, Value: {value} in {self.browserName} driver (Version {self.browserVersion}) on {self.platformName}")

    # def before_click(self, element, driver):
    #     """
    #         Called before clicking on an element.
    #
    #         Args:
    #             element: The element to be clicked.
    #             driver (webdriver.Chrome): The WebDriver instance.
    #     """
    #     customLogger.logger("INFO", f"Preparing to click on the element: {element} in {self.browserName} driver (Version {self.browserVersion}) on {self.platformName}")

    def after_click(self, element, driver):
        """
            Called after successfully clicking on an element.

            Args:
                element: The element that was clicked.
                driver (webdriver.Chrome): The WebDriver instance.
        """
        customLogger.logger("INFO", f"The element '{element}' was successfully clicked in {self.browserName} driver (Version {self.browserVersion}) on {self.platformName}")

    # def before_change_value_of(self, element, driver):
    #     """
    #         Called before changing the value of an element.
    #
    #         Args:
    #             element: The element whose value will be changed.
    #             driver (webdriver.Chrome): The WebDriver instance.
    #     """
    #     customLogger.logger("INFO", f"Preparing to change the value of the element: {element} in {self.browserName} driver (Version {self.browserVersion}) on {self.platformName}")

    def after_change_value_of(self, element, driver):
        """
            Called after successfully changing the value of an element.

            Args:
                element: The element whose value was changed.
                driver (webdriver.Chrome): The WebDriver instance.
        """
        customLogger.logger("INFO", f"The value of the element '{element}' was successfully changed in {self.browserName} driver (Version {self.browserVersion}) on {self.platformName}")

    # def before_execute_script(self, script, driver):
    #     """
    #         Called before executing a script in the browser.
    #
    #         Args:
    #             script (str): The script to be executed.
    #             driver (webdriver.Chrome): The WebDriver instance.
    #     """
    #     customLogger.logger("INFO", f"Preparing to execute the script: {script} in {self.browserName} driver (Version {self.browserVersion}) on {self.platformName}")

    def after_execute_script(self, script, driver):
        """
            Called after successfully executing a script in the browser.

            Args:
                script (str): The script that was executed.
                driver (webdriver.Chrome): The WebDriver instance.
        """
        customLogger.logger("INFO", f"The script '{script}' was executed successfully in the {self.browserName} browser (Version {self.browserVersion}) on {self.platformName}")

    # def before_close(self, driver):
    #     """
    #         Called before closing the browser.
    #
    #         Args:
    #             driver (webdriver.Chrome): The WebDriver instance.
    #     """
    #     customLogger.logger("INFO", f"Preparing to close the {self.browserName} browser (Version {self.browserVersion}) on {self.platformName}")

    def after_close(self, driver):
        """
            Called after successfully closing the browser.

            Args:
                driver (webdriver.Chrome): The WebDriver instance.
        """
        customLogger.logger("INFO", f"The {self.browserName} browser (Version {self.browserVersion}) on {self.platformName} has been successfully closed.")

    # def before_quit(self, driver):
    #     """
    #         Called before quitting the browser.
    #
    #         Args:
    #             driver (webdriver.Chrome): The WebDriver instance.
    #     """
    #     customLogger.logger("INFO", f"Preparing to quit the browser (Version {self.browserVersion}) on {self.platformName}")

    def after_quit(self, driver):
        """
            Called after successfully quitting the browser.

            Args:
                driver (webdriver.Chrome): The WebDriver instance.
        """
        customLogger.logger("INFO", f"The browser (Version {self.browserVersion}) on {self.platformName} has been successfully quit.")

    def on_exception(self, exception, driver):
        """
            Called when an exception occurs during WebDriver operations.

            Args:
                exception (Exception): The exception that occurred.
                driver (webdriver.Chrome): The WebDriver instance.
        """
        customLogger.logger("INFO", f"Exception occurred: {str(exception)} in {self.browserName} driver (Version {self.browserVersion}) on {self.platformName}")
