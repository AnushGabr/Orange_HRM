import time

from selenium.webdriver.common.by import By
from pom.base.base_page import BasePage
from pom.pages.navigation_panel import NavigationPanel
from selenium.webdriver import Keys


class MyInfoPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    MY_INFO_BUTTON = (By.XPATH, '//*[text() ="My Info"]')
    FIRST_INPUT_USERNAME = (By.CSS_SELECTOR, "input[name='firstName']")
    MIDNAME_INPUT_FIELD = (By.XPATH, "//input[@placeholder='Middle Name']")

    # variables for select-date

    CALENDAR_FIELD = (By.CSS_SELECTOR, 'div[class="oxd-date-input"]')
    CALENDAR_INPUT_FIELD = (By.CSS_SELECTOR, "div[class='oxd-date-input'] input")
    MONTH_DAYS = (By.CSS_SELECTOR, ".oxd-calendar-date-wrapper .oxd-calendar-date")

    ##
    MONTHS_AND_YEARS_DIV = (By.CSS_SELECTOR, ".oxd-calendar-dropdown")
    SELECT_MONTH_DIV = (By.CSS_SELECTOR, ".oxd-calendar-selector-month-selected")
    SELECT_YEAR_DIV = (By.CSS_SELECTOR, ".oxd-calendar-selector-year-selected i")
    SINGLE_MONTH_ID_FOR_ARRAY_CREATION = (By.CSS_SELECTOR, '.oxd-calendar-selector-month .oxd-calendar-dropdown--option')
    SINGLE_YEAR_ID_FOR_ARRAY_CREATION = (By.CSS_SELECTOR, ".oxd-calendar-dropdown .oxd-calendar-dropdown--option")


    # variables for nationality and marital status check

    NATIONALITY_AND_MARITAL_FIELD = (By.CSS_SELECTOR, ".oxd-select-text--arrow")
    NATIONALITY_AND_MARITAL_INPUT_FIELD = (By.CSS_SELECTOR, ".oxd-select-text .oxd-select-text-input")
    COUNTRIES_AND_MARITAL_DIV = (By.CSS_SELECTOR, "div[role='listbox']")
    COUNTRIES_LIST = (By.XPATH, "//div[@class='oxd-select-option']//span")
    SAVE_BUTTON = (By.CSS_SELECTOR, ".oxd-button")

    def init_my_info_page(self):
        navigation_panel = NavigationPanel(self.driver)
        navigation_panel.wait_for_page_load()
        navigation_panel.go_to("My_Info")

    # TODO: shift to selenium-driver
    # def clear_field(self, el):
    #     el.click()
    #     el.send_keys(Keys.CONTROL + 'a')
    #     el.send_keys(Keys.BACK_SPACE)

    def fill_first_username_field(self):
        element = self.get_wait().wait_for_element_to_be_clickable(self.FIRST_INPUT_USERNAME)
        self.clear_field(element)
        element.click()
        element.send_keys("Mark")

    def is_first_input_field_valid(self):
        field = self.find_element_by(self.FIRST_INPUT_USERNAME)
        return field.get_attribute('value') == 'Mark'

    def fill_midname_input_field(self):
        element = self.get_wait().wait_for_element_to_be_clickable(self.MIDNAME_INPUT_FIELD)
        self.clear_field(element)
        element.click()
        element.send_keys('John')

    def is_midname_input_field_valid(self):
        field = self.find_element_by(self.MIDNAME_INPUT_FIELD)
        return field.get_attribute('value') == 'John'

    def select_date(self):
        element = self.get_wait().wait_for_element_to_be_clickable(self.CALENDAR_FIELD)
        element.click()

        month_selection_part = self.get_wait().wait_for_element_to_be_clickable(self.SELECT_MONTH_DIV)
        month_selection_part.click()
        option_list_months = self.get_wait().wait_for_list_size_change(self.SINGLE_MONTH_ID_FOR_ARRAY_CREATION, size=12)

        for month in option_list_months:
            current = month.get_attribute('innerText')
            if current == 'March':
                month.click()
                break

        year_selection_part = self.get_wait().wait_for_element_to_be_clickable(self.SELECT_YEAR_DIV)
        # self.driver.execute_script('arguments[0]․click();', year_selection_part)
        year_selection_part.click()

        option_list_year = self.get_wait().wait_for_list_size_change(self.SINGLE_YEAR_ID_FOR_ARRAY_CREATION, size=54)

        for year in option_list_year:
            current = year.get_attribute('innerText')
            if current == '2020':
                self.driver.execute_script("arguments[0].click();", year)
                # year.click()
                break

        option_list_day = self.find_list_of_elements(self.MONTH_DAYS)

        for option in option_list_day:
            current = option.text
            if current == '15':
                option.click()
                break

    # FIXME: check again something is not ok
    def is_selected_date_correct(self):
        field = self.find_element_by(self.CALENDAR_INPUT_FIELD)
        return field.get_attribute('value') == '03-15-2020'

    def choose_nationality(self):
        element = self.get_wait().wait_for_list_size_change(self.NATIONALITY_AND_MARITAL_FIELD, size=3)
        icon = element[0]
        icon.click()

        option_to_choose = "Haitian"
        div = self.get_wait().wait_for_element_to_be_clickable(self.COUNTRIES_AND_MARITAL_DIV)
        option_list = self.find_list_of_elements(self.COUNTRIES_LIST)

        for option in option_list:
            current = option.text

            if current == option_to_choose:
                option.click()
                break

    def is_nationality_field_correct(self):
        field = self.find_element_by(self.NATIONALITY_AND_MARITAL_INPUT_FIELD)
        return field.text == 'Haitian'

    def select_marital_status_field(self):
        inputs = self.get_wait().wait_for_list_size_change(self.NATIONALITY_AND_MARITAL_FIELD, size=3)
        marital_status_input = inputs[1]
        marital_status_input.click()
        option_div = self.get_wait().wait_for_element_to_be_clickable(self.COUNTRIES_AND_MARITAL_DIV)
        option_list = self.find_list_of_elements(self.COUNTRIES_LIST)
        option_to_choose = "Married"

        for option in option_list:
            current = option.text

            if current == option_to_choose:
                option.click()
                break

    def is_marital_status_correct(self):
        fields = self.find_list_of_elements(self.NATIONALITY_AND_MARITAL_INPUT_FIELD)
        marital_input = fields[1]

        return marital_input.text == 'Married'

    def save_all_fields_info(self):
        save_button = self.get_wait().wait_for_element_to_be_clickable(self.SAVE_BUTTON)
        save_button.click()
