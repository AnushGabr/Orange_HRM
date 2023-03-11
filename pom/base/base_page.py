from selenium.webdriver import ActionChains
from pom.base.selenium_driver import SeleniumDriver
from pom.wait.wait import Wait


class BasePage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.wait = Wait(self.driver, 30)

    def get_wait(self):
        return self.wait

    def get_actions(self):
        return ActionChains(self.driver)

    def wait_for_page_load(self):
        self.get_wait().wait_for_page()

