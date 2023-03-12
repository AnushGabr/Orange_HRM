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
    # CALENDAR_OPENED_WHOLE_DIV = (By.CSS_SELECTOR, ".oxd-date-input-calendar")
    MONTH_DAYS = (By.CSS_SELECTOR, ".oxd-calendar-date-wrapper .oxd-calendar-date")
    # MONTH_DROPDOWN_DIV = (By.CSS_SELECTOR, ".oxd-calendar-selector-month .oxd-calendar-dropdown")
    ##
    MONTHS_AND_YEARS_DIV = (By.CSS_SELECTOR, ".oxd-calendar-dropdown")
    SELECT_MONTH_DIV = (By.CSS_SELECTOR, ".oxd-calendar-selector-month-selected")
    SELECT_YEAR_DIV = (By.CSS_SELECTOR, ".oxd-calendar-selector-year-selected")
    SINGLE_MONTH_ID_FOR_ARRAY_CREATION = (By.CSS_SELECTOR, '.oxd-calendar-selector-month .oxd-calendar-dropdown--option')
    SINGLE_YEAR_ID_FOR_ARRAY_CREATION = (By.CSS_SELECTOR, ".oxd-calendar-dropdown .oxd-calendar-dropdown--option")
    # SINGLE_DAY_ID_FOR_ARRAY_CREATION = (By.CSS_SELECTOR, '.oxd-calendar-dates-grid')

    # variables for nationality and marital status check

    NATIONALITY_AND_MARITAL_FIELD = (By.CSS_SELECTOR, ".oxd-select-text")
    NATIONALITY_AND_MARITAL_INPUT_FIELD = (By.CSS_SELECTOR, ".oxd-select-text .oxd-select-text-input")
    COUNTRIES_AND_MARITAL_DIV = (By.CSS_SELECTOR, "div[role='listbox']")
    COUNTRIES_LIST = (By.XPATH, "//div[@class='oxd-select-option']//span")
    # GENDER_BUTTON = (By.CSS_SELECTOR, ".oxd-radio-wrapper label")
    # check_gender_button = (By.CSS_SELECTOR, "input[type=radio]")

    SAVE_BUTTON = (By.CSS_SELECTOR, ".oxd-button")

    def init_my_info_page(self):
        navigation_panel = NavigationPanel(self.driver)
        navigation_panel.wait_for_page_load()
        navigation_panel.go_to("My_Info")

    # TODO: shift to selenium-driver
    def clear_field(self, el):
        el.send_keys(Keys.CONTROL + 'a')
        el.send_keys(Keys.BACK_SPACE)

    def fill_first_username_field(self):
        element = self.get_wait().wait_for_element_to_be_clickable(self.FIRST_INPUT_USERNAME)
        self.clear_field(element)
        element.send_keys("Mark")

    def is_first_input_field_valid(self):
        field = self.find_element_by(self.FIRST_INPUT_USERNAME)
        return field.get_attribute('value') == 'Mark'

    def fill_midname_input_field(self):
        element = self.get_wait().wait_for_element_to_be_clickable(self.MIDNAME_INPUT_FIELD)
        self.clear_field(element)
        element.send_keys('John')

    def is_midname_input_field_valid(self):
        field = self.find_element_by(self.MIDNAME_INPUT_FIELD)
        return field.get_attribute('value') == 'John'

    def select_date(self):
        element = self.get_wait().wait_for_element_to_be_clickable(self.CALENDAR_FIELD)
        element.click()
        # self.driver.execute_script("arguments[0].click();", element)
        # calendar_div = self.get_wait().wait_for_element_to_be_clickable(self.CALENDAR_OPENED_WHOLE_DIV)
        month_li = self.get_wait().wait_for_element_to_be_clickable(self.SELECT_MONTH_DIV)
        month_li.click()
        # month_dyn_div = self.get_wait().wait_for_element_to_be_clickable(self.MONTH_DROPDOWN_DIV)
        # option_list_months = self.find_list_of_elements(self.months)
        option_list_months = self.get_wait().wait_for_list_size_change(self.SINGLE_MONTH_ID_FOR_ARRAY_CREATION, size=12)

        for month in option_list_months:
            current = month.get_attribute('innerText')
            if current == 'March':
                month.click()
                break

        year_selection_part = self.get_wait().wait_for_element_to_be_clickable(self.SELECT_YEAR_DIV)
        year_selection_part.click()
        year_and_month_div = self.find_list_of_elements(self.MONTHS_AND_YEARS_DIV)
        only_year_div = year_and_month_div[1]
        year = self.get_wait().wait_for_element_to_be_clickable(only_year_div)
        # year_dyn_div = self.get_wait().wait_for_element_to_be_clickable(self.CALENDAR_DYNAMIC_YEAR)
        option_list_year = self.find_list_of_elements(self.SINGLE_YEAR_ID_FOR_ARRAY_CREATION)

        for year in option_list_year:
            current = year.get_attribute('innerText')
            if current == '2020':
                year.click()
                break

        # days = self.get_wait().wait_for_element_to_be_clickable(self.SINGLE_DAY_ID_FOR_ARRAY_CREATION)
        option_list_day = self.find_list_of_elements(self.MONTH_DAYS)

        for option in option_list_day:
            current = option.text
            if current == '15':
                option.click()
                break

    # FIXME: check again something is not ok
    def is_selected_date_correct(self):
        field = self.find_element_by(self.CALENDAR_INPUT_FIELD)
        return field.get_attribute('value') == '2020-03-15'

    def choose_nationality(self):
        element = self.get_wait().wait_for_element_to_be_clickable(self.NATIONALITY_AND_MARITAL_FIELD)
        element.click()

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
        inputs = self.find_list_of_elements(self.NATIONALITY_AND_MARITAL_FIELD)
        marital_status_input = inputs[1].click()
        option_div = self.get_wait().wait_for_element_to_be_clickable(self.COUNTRIES_AND_MARITAL_DIV)
        option_list = self.find_list_of_elements(self.COUNTRIES_LIST)
        option_to_choose = "Single"

        for option in option_list:
            current = option.text

            if current == option_to_choose:
                option.click()
                break

    def is_marital_status_correct(self):
        fields = self.find_list_of_elements(self.NATIONALITY_AND_MARITAL_INPUT_FIELD)
        marital_input = fields[1]

        return marital_input.text == 'Single'

    # def gender_field(self):
    #     radio_button = self.get_wait().wait_for_element_to_be_clickable(self.GENDER_BUTTON)
    #     self.driver.execute_script("arguments[0].click();", radio_button)
    #
    # def gender_field_correct(self):
    #     element = self.is_element_selected(self.check_gender_button)
    #     return element

    def save_all_fields_info(self):
        save_button = self.get_wait().wait_for_element_to_be_clickable(self.SAVE_BUTTON)
        save_button.click()
