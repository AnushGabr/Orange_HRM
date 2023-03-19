from selenium.webdriver.common.by import By
from pom.base.base_page import BasePage
from pom.pages.navigation_panel import NavigationPanel
from pom.pages.admin.admin_header import AdminHeader


class Admin(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    ADMIN_HEADER_SECTIONS = (By.CSS_SELECTOR, ".oxd-topbar-body-nav-tab span i")
    ORGANIZATION_MENU = (By.CSS_SELECTOR, ".oxd-dropdown-menu")
    GENERAL_INFO_OPTION = (By.CSS_SELECTOR, ".oxd-dropdown-menu li")
    EDIT_BUTTON = (By.CSS_SELECTOR, ".oxd-switch-input")
    INPUT_FIELDS = (By.CSS_SELECTOR, ".oxd-input--active")

    def init_admin_page(self):
        self.driver.maximize_window()
        navigation_panel = NavigationPanel(self.driver)
        navigation_panel.wait_for_page_load()
        navigation_panel.go_to("Admin")

    def init_admin_page_header(self):
        admin_header = AdminHeader(self.driver)
        admin_header.go_to('Organization')

    def click_organization(self):
        dropdown_menu = self.get_wait().wait_for_element_to_be_clickable(self.ORGANIZATION_MENU)
        gen_info_option = self.find_element_by(self.GENERAL_INFO_OPTION)
        gen_info_option.click()

        edit_button = self.get_wait().wait_for_element_to_be_clickable(self.EDIT_BUTTON)
        edit_button.click()

    def changing_organization_name(self):
        inputs_list = self.get_wait().wait_for_list_size_change(self.INPUT_FIELDS, size=12)
        organization_input = inputs_list[1]
        self.clear_field(organization_input)
        organization_input.send_keys('Armenian HR')

    def changing_registration_number(self):
        inputs_list = self.get_wait().wait_for_list_size_change(self.INPUT_FIELDS, size=12)
        registration_number_field = inputs_list[2]
        self.clear_field(registration_number_field)
        registration_number_field.send_keys('55555')
