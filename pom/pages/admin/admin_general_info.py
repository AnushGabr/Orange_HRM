from selenium.webdriver.common.by import By
from pom.base.base_page import BasePage
from pom.pages.navigation_panel import NavigationPanel
from selenium.webdriver import Keys


class Admin(BasePage):

    def __init__(self, driver):
        super().__init__(driver)


    ADMIN_HEADER_SECTIONS = (By.CSS_SELECTOR, ".oxd-topbar-body-nav-tab span i")
    ORGANIZATION_MENU = (By.CSS_SELECTOR, ".oxd-dropdown-menu")
    GENERAL_INFO_OPTION = (By.CSS_SELECTOR, ".oxd-dropdown-menu li")
    EDIT_BUTTON = (By.CSS_SELECTOR, ".oxd-switch-input")

    def init_admin_page(self):
        self.driver.maximize_window()
        navigation_panel = NavigationPanel(self.driver)
        navigation_panel.wait_for_page_load()
        navigation_panel.go_to("Admin")

    def click_organization(self):
        button_list = self.get_wait().wait_for_list_size_change(self.ADMIN_HEADER_SECTIONS, size=5)
        button_list[2].click()

        dropdown_menu = self.get_wait().wait_for_element_to_be_clickable(self.ORGANIZATION_MENU)
        gen_info_option = self.find_element_by(self.GENERAL_INFO_OPTION)
        gen_info_option.click()

        edit_button = self.get_wait().wait_for_element_to_be_clickable(self.EDIT_BUTTON)
        edit_button.click()

    #Todo:after this elements should be selected than changing info and save after that checking correct or not


