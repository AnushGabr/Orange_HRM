import selenium.common.exceptions as Ex
from selenium.webdriver import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.select import Select


class SeleniumDriver:

    def __init__(self, driver):
        self.driver: WebDriver = driver

    def refresh_page(self):
        self.driver.refresh()

    def navigate_to_url(self, url: str):
        self.driver.get(url)

    def find_element_by(self, locator):
        element = None
        try:
            element = self.driver.find_element(*locator)
        except Ex.NoSuchElementException:
            print('Element is not found')

        return element

    def find_list_of_elements(self, locator):
        elements = None
        try:
            elements = self.driver.find_elements(*locator)
        except Ex.NoSuchElementException:
            print('Elements are not found')

        return elements

    def click(self, element):
        if element:
            try:
                element.click()
                return True
            except (Ex.NoSuchElementException, Ex.ElementClickInterceptedException,
                    Ex.ElementNotInteractableException) as error:
                print(error)
                return False

        return False

    def clear_field(self, element):
        if element:
            try:
                element.click()
                element.send_keys(Keys.CONTROL + 'a')
                element.send_keys(Keys.BACK_SPACE)
                return True
            except:
                print('NoSuchElement clear field')
                return False
        return False

    def is_element_displayed(self, locator):
        displayed = False

        if locator:
            element = self.driver.find_element(*locator)
            try:
                displayed = element.is_displayed()
            except (Ex.NoSuchElementException, Ex.ElementNotVisibleException) as error:
                print("Element is not displayed: Error: " + error)

        return displayed

    def is_element_selected(self, locator):
        selected = False

        if locator:
            element = self.driver.find_element(*locator)
            try:
                selected = element.is_selected()
            except Ex.NoSuchElementException:
                print('Element is not selected')

        return selected
