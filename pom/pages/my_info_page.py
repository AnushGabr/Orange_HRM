from selenium.webdriver.common.by import By
from pom.base.base_page import BasePage
from pom.pages.navigation_panel import NavigationPanel
from selenium.webdriver import Keys


class MyInfoPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    MY_INFO_BUTTON = (By.XPATH, '//*[text() ="My Info"]')
    SAVE_BUTTON = (By.CSS_SELECTOR, ".oxd-button")
    FIRST_INPUT_USERNAME = (By.CSS_SELECTOR, "input[name='firstName']")
    MIDNAME_INPUT_FIELD = (By.XPATH, "//input[@placeholder='Middle Name']")
    CALENDAR_INPUT_FIELD = (By.CSS_SELECTOR, 'div[class="oxd-date-input"]')
    CALENDAR_DYNAMIC_DIV = (By.CSS_SELECTOR, ".oxd-date-input-calendar",)

    def init_my_info_page(self):
        navigation_panel = NavigationPanel(self.driver)
        navigation_panel.wait_for_page_load()
        navigation_panel.go_to("My_Info")

    # selenium-driver mej texapoxel
    def clear_field(self, el):
        el.send_keys(Keys.CONTROL + 'a')
        el.send_keys(Keys.BACK_SPACE)

    def first_input_field(self):
        element = self.get_wait().wait_for_element_to_be_clickable(self.FIRST_INPUT_USERNAME)
        self.clear_field(element)
        element.send_keys("Clark")

    def is_first_input_field_valid(self):
        field = self.find_element_by(self.FIRST_INPUT_USERNAME)
        return field.get_attribute('value') == 'Clark'

    # def midname_input_field(self):
    #     element = self.get_wait().wait_for_element_to_be_clickable(self.MIDNAME_INPUT_FIELD)
    #     self.clear_field(element)
    #
    # def calendar_field(self):
    #     element = self.get_wait().wait_for_element_to_be_clickable(self.CALENDAR_INPUT_FIELD)
    #     element.click()
    #
    #     calendar_div = self.get_wait().wait_for_element_to_be_clickable(self.CALENDAR_DYNAMIC_DIV)
