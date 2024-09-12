from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementClickInterceptedException
from selenium.webdriver.common.action_chains import ActionChains

from common_.utilities_ import customLogger


class BasePage:
    def __init__(self, driver):
        """
            Initialize the BasePage with a Selenium WebDriver instance.

            Args:
                driver (selenium.webdriver.remote.webdriver.WebDriver): The Selenium WebDriver instance used for web automation.
        """
        self.driver = driver

    def _find_element(self, locator, timeout=10, condition=EC.visibility_of_element_located):
        """
            Finds and returns a web element based on the provided locator, waiting for a specified condition.
        """
        from exitCodes import MessageCodes, ELEMENT_NOT_FOUND, TIMEOUT_ERROR, UNEXPECTED_BEHAVIOR
        try:
            element = WebDriverWait(self.driver, timeout).until(condition(locator))
            return element
        except NoSuchElementException as e:
            customLogger.logger("ERROR", f"{MessageCodes[ELEMENT_NOT_FOUND]} - {str(e)}")
            exit(ELEMENT_NOT_FOUND)
        except TimeoutException as e:
            customLogger.logger("ERROR", f"{MessageCodes[TIMEOUT_ERROR]} - {str(e)}")
            exit(TIMEOUT_ERROR)
        except Exception as e:
            customLogger.logger("ERROR", f"{MessageCodes[UNEXPECTED_BEHAVIOR]} -  {str(e)}")
            exit(UNEXPECTED_BEHAVIOR)

    def _mouse_move_to_element(self, element):
        """
            Moves the mouse cursor to a specified element on the web page.
        """
        action = ActionChains(self.driver)
        action.move_to_element(element)
        action.perform()

    def _mouse_move_by_offset(self, x, y):
        """
            Moves the mouse cursor by a specified offset from its current position.
        """
        action = ActionChains(self.driver)
        action.move_by_offset(x, y)
        action.perform()

    def _get_title_(self):
        """
            Gets the title of the current web page.
        """
        return self.driver.title

    def _fill_field(self, element, text):
        """
            Fills the text input field with the provided text after clearing its current content.
        """
        element.clear()
        element.send_keys(text)

    def _fill_field_and_apply(self, element, text, key):
        """
            Fills the form field with text and apply a key action.
            Example Usage:
                # Input text and press Enter key using _fill_field_and_apply method
                    text_to_input = "Hello, World!"
                    _fill_field_and_apply(input_field, text_to_input, Keys.ENTER)
        """
        self._fill_field(element, text)
        element.send_keys(key)

    def _click_to_element(self, element):
        """
            Performs a click on a web element after ensuring its clickable.
            Note:
                -The method waits for the element to be both enabled and displayed before clicking it.
        """
        from exitCodes import MessageCodes, TIMEOUT_ERROR, ELEMENT_CLICK_INTERCEPTED, UNEXPECTED_BEHAVIOR
        try:
            WebDriverWait(self.driver, 10).until(lambda driver: element.is_enabled() and element.is_displayed())
            element.click()
        except TimeoutException as e:
            customLogger.logger("ERROR", f"{MessageCodes[TIMEOUT_ERROR]} - {str(e)}")
            exit(TIMEOUT_ERROR)
        except ElementClickInterceptedException as e:
            customLogger.logger("ERROR", f"{MessageCodes[ELEMENT_CLICK_INTERCEPTED]} -  {str(e)}")
            exit(ELEMENT_CLICK_INTERCEPTED)
        except Exception as e:
            customLogger.logger("ERROR", f"{MessageCodes[UNEXPECTED_BEHAVIOR]} -  {str(e)}")
            exit(UNEXPECTED_BEHAVIOR)

    def _get_element_text(self, element):
        """
            Gets the text content of a web element.
        """
        return element.text

    def _double_click_to_element(self, element):
        """
            Performs a double click on a web element after ensuring it is clickable(enabled and displayed).
            Note:
                -This method uses ActionChains to perform the double click action.
        """
        from exitCodes import MessageCodes, TIMEOUT_ERROR, ELEMENT_CLICK_INTERCEPTED, UNEXPECTED_BEHAVIOR
        try:
            WebDriverWait(self.driver, 10).until(lambda driver: element.is_enabled() and element.is_displayed())
            action = ActionChains(self.driver)
            action.double_click(element)
            action.perform()
        except TimeoutException as e:
            customLogger.logger("ERROR", f"{MessageCodes[TIMEOUT_ERROR]} - {str(e)}")
            exit(TIMEOUT_ERROR)
        except ElementClickInterceptedException as e:
            customLogger.logger("ERROR", f"{MessageCodes[ELEMENT_CLICK_INTERCEPTED]} -  {str(e)}")
            exit(ELEMENT_CLICK_INTERCEPTED)
        except Exception as e:
            customLogger.logger("ERROR", f"{MessageCodes[UNEXPECTED_BEHAVIOR]} -  {str(e)}")
            exit(UNEXPECTED_BEHAVIOR)

    def _is_element_present(self, locator, timeout=10):
        """
            Checks if the given element identified by the provided locator is present on the web page.
        """
        try:
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
            return True
        except:
            customLogger.logger("INFO", f"The corresponding element is missing")
            return False

    def _element_should_be_present(self, locator, timeout=10):
        """
            This method assumes that a given element, identified by the provided locator, must be present on the web page.
        """
        from exitCodes import MessageCodes, ELEMENT_NOT_FOUND, TIMEOUT_ERROR, UNEXPECTED_BEHAVIOR
        try:
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
        except NoSuchElementException as e:
            customLogger.logger("ERROR", f"{MessageCodes[ELEMENT_NOT_FOUND]} - {str(e)}")
            exit(ELEMENT_NOT_FOUND)
        except TimeoutException as e:
            customLogger.logger("ERROR", f"{MessageCodes[TIMEOUT_ERROR]} - {str(e)}")
            exit(TIMEOUT_ERROR)
        except Exception as e:
            customLogger.logger("ERROR", f"{MessageCodes[UNEXPECTED_BEHAVIOR]} -  {str(e)}")
            exit(UNEXPECTED_BEHAVIOR)

    def _is_element_visible(self, locator, timeout=10):
        """
            Checks if the given element identified by the provided locator is visible on the web page.
        """
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            return True
        except:
            customLogger.logger("INFO", f"The corresponding element is not visible")
            return False

    def _element_should_be_visible(self, locator, timeout=10):
        """
            This method assumes that a given element, identified by the provided locator, must be visible on the web page.
        """
        from exitCodes import MessageCodes, ELEMENT_NOT_FOUND, TIMEOUT_ERROR, UNEXPECTED_BEHAVIOR
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        except NoSuchElementException as e:
            customLogger.logger("ERROR", f"{MessageCodes[ELEMENT_NOT_FOUND]} - {str(e)}")
            exit(ELEMENT_NOT_FOUND)
        except TimeoutException as e:
            customLogger.logger("ERROR", f"{MessageCodes[TIMEOUT_ERROR]} - {str(e)}")
            exit(TIMEOUT_ERROR)
        except Exception as e:
            customLogger.logger("ERROR", f"{MessageCodes[UNEXPECTED_BEHAVIOR]} -  {str(e)}")
            exit(UNEXPECTED_BEHAVIOR)

    def _get_attribute(self, element, attribute):
        """
            Waits for the specified attribute of the given element to be updated with a non-empty value and returns it.
        """
        from exitCodes import MessageCodes, TIMEOUT_ERROR, UNEXPECTED_BEHAVIOR
        try:
            WebDriverWait(self.driver, 10).until(lambda driver: element.get_attribute(attribute))
            return element.get_attribute(attribute)
        except TimeoutException as e:
            customLogger.logger("ERROR", f"{MessageCodes[TIMEOUT_ERROR]} - {str(e)}")
            exit(TIMEOUT_ERROR)
        except Exception as e:
            customLogger.logger("ERROR", f"{MessageCodes[UNEXPECTED_BEHAVIOR]} -  {str(e)}")
            exit(UNEXPECTED_BEHAVIOR)
