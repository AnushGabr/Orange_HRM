from selenium.webdriver.common.by import By
from pom.base.base_page import BasePage
from pom.pages.navigation_panel import NavigationPanel
from pom.pages.admin.admin_header import AdminHeader


class Memberships(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    ADMIN_HEADER_SECTIONS = (By.CSS_SELECTOR, ".oxd-topbar-body-nav-tab span i")
    QUALIFICATION_MENU = (By.CSS_SELECTOR, "ul[class = 'oxd-dropdown-menu']")
    MEMBERSHIPS_OPTION = (By.XPATH, '//a[text()= "Memberships"]')
    ADD_BUTTON = (By.CSS_SELECTOR, "button[class$='oxd-button--secondary']")
    ADD_INPUT_FIELD = (By.XPATH, '(//input[@class="oxd-input oxd-input--active"])[2]')
    SAVE_BUTTON = (By.CSS_SELECTOR, 'button[type="submit"]')
    MEMBERSHIPS_TEXT = (By.XPATH, '//div[text()= "The Australian Computer Society"]')

    def init_admin_page(self):
        self.driver.maximize_window()
        navigation_panel = NavigationPanel(self.driver)
        navigation_panel.wait_for_page_load()
        navigation_panel.go_to("Admin")

    def init_admin_page_header(self):
        admin_header = AdminHeader(self.driver)
        admin_header.go_to('Qualifications')

    def click_qualification(self):

        memberships_option = self.get_wait().wait_for_element_to_be_clickable(self.MEMBERSHIPS_OPTION)
        memberships_option.click()



    def adding_new_membership(self):
        try:
            added_member = self.get_wait().wait_for_element(self.MEMBERSHIPS_TEXT)
            added_member.click()

        except:
            add_button = self.get_wait().wait_for_element_to_be_clickable(self.ADD_BUTTON)
            add_button.click()

            add_member_input = self.get_wait().wait_for_element_to_be_clickable(self.ADD_INPUT_FIELD)
            add_member_input.click()
            self.clear_field(add_member_input)
            add_member_input.send_keys('The Australian Computer Society')
            save_button = self.get_wait().wait_for_element_to_be_clickable(self.SAVE_BUTTON)
            save_button.click()
            added_member = self.get_wait().wait_for_element(self.MEMBERSHIPS_TEXT)
            added_member.click()
