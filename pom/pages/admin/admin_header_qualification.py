from selenium.webdriver.common.by import By
from pom.base.base_page import BasePage
from pom.pages.navigation_panel import NavigationPanel
from pom.pages.admin.admin_header import AdminHeader


class Admin(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    ADMIN_HEADER_SECTIONS = (By.CSS_SELECTOR, ".oxd-topbar-body-nav-tab span i")
    QUALIFICATION_MENU = (By.CSS_SELECTOR, "ul[class = 'oxd-dropdown-menu']")
    EDUCATION_OPTION = (By.XPATH, '//a[text()= "Education"]')
    ADD_BUTTON = (By.CSS_SELECTOR, "button[class$='menu-button']")
    ADD_INPUT_FIELD = (By.XPATH, '(//input[@class="oxd-input oxd-input--active"])[2]')
    SAVE_BUTTON = (By.CSS_SELECTOR, 'button[type="submit"]')


    def init_admin_page(self):
        self.driver.maximize_window()
        navigation_panel = NavigationPanel(self.driver)
        navigation_panel.wait_for_page_load()
        navigation_panel.go_to("Admin")

    def init_admin_page_header(self):
        admin_header = AdminHeader(self.driver)
        admin_header.go_to('Qualifications')

    def click_qualification(self):
        main_dropdawn_menu = self.get_wait().wait_for_list_size_change(self.ADMIN_HEADER_SECTIONS, size=4)
        qualification_dropdown = main_dropdawn_menu[3]
        qualification_dropdown.click()
        qualif_menu = self.get_wait().wait_for_element_to_be_clickable(self.QUALIFICATION_MENU)
        education_option = self.find_element_by(self.EDUCATION_OPTION)
        education_option.click()

        add_button = self.get_wait().wait_for_element_to_be_clickable(self.ADD_BUTTON)
        add_button.click()

    def adding_new_education(self):
        add_educ_input = self.get_wait().wait_for_element_to_be_clickable(self.ADD_INPUT_FIELD)
        self.clear_field(add_educ_input)
        add_educ_input.send_keys('Doctorate/PhD')
        self.SAVE_BUTTON.click()

