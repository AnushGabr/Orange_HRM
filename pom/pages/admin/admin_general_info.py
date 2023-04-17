from selenium.webdriver.common.by import By
from pom.base.base_page import BasePage
from pom.pages.navigation_panel import NavigationPanel
from pom.pages.admin.admin_header import AdminHeader


class Admin(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    #ADMIN_HEADER_SECTIONS = (By.CSS_SELECTOR, ".oxd-topbar-body-nav-tab span i")
    ADMIN_HEADER_ORGANIZATION_MENU = (By.CSS_SELECTOR, ".oxd-dropdown-menu")
    ORGANIZATION_MENU_GENERAL_INFO_OPTION = (By.CSS_SELECTOR, ".oxd-dropdown-menu li")
    EDIT_BUTTON = (By.CSS_SELECTOR, ".oxd-switch-input")
    INPUT_FIELDS = (By.CSS_SELECTOR, ".oxd-input--active")
    SAVE_BUTTON = (By.CSS_SELECTOR, '.oxd-button--medium')
    COUNTRY_BUTTON = (By.CSS_SELECTOR, '.oxd-select-text i')
    COUNTRY_INPUT = (By.CSS_SELECTOR, '.oxd-select-text-input')

    COUNTRTY_DIV = (By.CSS_SELECTOR, ".oxd-select-dropdown")
    COUNTRTY_LIST = (By.CSS_SELECTOR, '.oxd-select-option')

    TEXTAREA = (By.CSS_SELECTOR, '.oxd-textarea')

    input_address_for_check = (By.CSS_SELECTOR, '.oxd-input-field-bottom-space input')

    def init_admin_page(self):
        self.driver.maximize_window()
        navigation_panel = NavigationPanel(self.driver)
        navigation_panel.wait_for_page_load()
        navigation_panel.go_to("Admin")

    def init_admin_page_header(self):
        admin_header = AdminHeader(self.driver)
        admin_header.go_to('Organization')

    def click_organization(self):
        dropdown_menu = self.get_wait().wait_for_element_to_be_clickable(self.ADMIN_HEADER_ORGANIZATION_MENU)
        gen_info_option = self.find_element_by(self.ORGANIZATION_MENU_GENERAL_INFO_OPTION)
        gen_info_option.click()

        edit_button = self.get_wait().wait_for_element_to_be_clickable(self.EDIT_BUTTON)
        edit_button.click()

    def changing_organization_name(self):
        inputs_list = self.get_wait().wait_for_list_size_change(self.INPUT_FIELDS, size=12)
        organization_input = inputs_list[1]
        self.clear_field(organization_input)
        organization_input.send_keys('Armenian HR')

    def get_input_field(self, index):
        input_list = self.find_list_of_elements(self.INPUT_FIELDS)
        return input_list[index]

    def check_organization_name_is_correct(self):
        organization_name_field = self.get_input_field(1)
        return organization_name_field.get_attribute('value') == 'Armenian HR'

    def changing_email(self):
        email_input = self.get_input_field(5)
        self.clear_field(email_input)
        email_input.send_keys('g@gmail.com')

    def check_email_is_correct(self):
        # email_field = self.get_input_field(5)
        # print(email_field.text)
        list = self.find_list_of_elements(self.input_address_for_check)
        return list[5].get_attribute('value') == 'g@gmail.com'

    def changing_address(self):
        address_input = self.get_input_field(7)
        self.clear_field(address_input)
        address_input.send_keys('Kochar')

    def check_address_is_correct(self):
        #
        # registration_number_field = self.get_input_field(7)
        # return registration_number_field.get_attribute('value') == 'Kochar'

        list = self.find_list_of_elements(self.input_address_for_check)
        return list[7].get_attribute('value') == 'Kochar'

    def changing_city(self):
        city_input = self.get_input_field(8)
        self.clear_field(city_input)
        city_input.send_keys('Yerevan')

    def changing_country(self):
        option_to_choose = "Cameroon"
        icon = self.get_wait().wait_for_element_to_be_clickable(self.COUNTRY_BUTTON)
        icon.click()

        self.get_wait().wait_for_element_to_be_clickable(self.COUNTRTY_DIV)
        option_list = self.find_list_of_elements(self.COUNTRTY_LIST)

        for option in option_list:
            current = option.text

            if current == option_to_choose:
                option.click()
                break

    def check_nationality_correct(self):
        input_field = self.find_element_by(self.COUNTRY_INPUT)
        return input_field.text == 'Cameroon'

    def fill_textarea(self):
        text_area = self.get_wait().wait_for_element_to_be_clickable(self.TEXTAREA)
        self.clear_field(text_area)
        text_area.send_keys('Its my personal information')

    def check_textarea(self):
        text_area = self.get_wait().wait_for_element_to_be_clickable(self.TEXTAREA)
        return text_area.get_attribute('value') == 'Its my personal information'

    def saving(self):
        save_button = self.get_wait().wait_for_element_to_be_clickable(self.SAVE_BUTTON)
        self.driver.execute_script("arguments[0].click();", save_button)
