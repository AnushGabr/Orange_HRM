from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as condition

from pom.base.selenium_driver import SeleniumDriver


class Wait:

    def __init__(self, driver, timeout):
        self.driver: WebDriver = driver
        self.wait = WebDriverWait(self.driver, timeout)

    def wait_for_element(self, locator):
        element = None
        try:
            element = self.wait.until(condition.visibility_of_element_located(locator))
        except NoSuchElementException:
            print('element is not found')
        return element

    def wait_for_element_to_be_clickable(self, locator,):
        element = None
        try:
            element = self.wait.until(condition.element_to_be_clickable(locator))
        except NoSuchElementException:
            print('element not found')
        return element

    def wait_for_element_to_be_selected(self, element):
        selected_element = None
        try:
            selected_element = self.wait.until(condition.element_selection_state_to_be(element, True))
        except NoSuchElementException:
            print('No selected element')
        return selected_element

    def wait_for_list_size_change(self, locator, size):
        """
        Wait for the size of a list of elements to change to a specific value.
        Args
            locator: a tuple (By.<method>, <selector>) that identifies the list of elements
            size: an integer representing the expected size of the list of elements
        Raises:
            TimeoutException if the size of the list of elements does not change to the expected value
        """

        try:
            self.wait.until(lambda driver: len(driver.find_elements(*locator)) == size)
            return self.driver.find_elements(*locator)
        except TimeoutException:
            print(f"Timed out waiting for {size} elements to be present")
            return False

    def wait_for_page(self):
        try:
            self.wait.until(lambda driver: driver.execute_script("return document.readyState") == 'complete')
        except:
            print('Document is not ready yet')


