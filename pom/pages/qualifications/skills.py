from selenium.webdriver.common.by import By
from pom.base.base_page import BasePage
from pom.pages.navigation_panel import NavigationPanel
from pom.pages.admin.admin_header import AdminHeader


class Skills(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    ADMIN_HEADER_SECTIONS = (By.CSS_SELECTOR, ".oxd-topbar-body-nav-tab span i")
    QUALIFICATION_MENU = (By.CSS_SELECTOR, "ul[class = 'oxd-dropdown-menu']")
    SKILLS_OPTION = (By.XPATH, '//a[text()= "Skills"]')
    ADD_BUTTON = (By.CSS_SELECTOR, "button[class$='oxd-button--secondary']")
    ADD_NAME_FIELD = (By.XPATH, '(//input[@class="oxd-input oxd-input--active"])[2]')
    ADD_DESCRIPTION_FIELD = (By.CSS_SELECTOR, 'textarea[placeholder="Type description here"]')
    SAVE_BUTTON = (By.CSS_SELECTOR, 'button[type="submit"]')
    SKILL_TEXT = (By.XPATH, '//div[text()= "Python"]')
    DESCRIPTION_FIELD = (By.CSS_SELECTOR, 'textarea[placeholder="Type description here"]')
    DESCRIPTION_TEXT = 'Propramming Language'

    def init_admin_page(self):
        self.driver.maximize_window()
        navigation_panel = NavigationPanel(self.driver)
        navigation_panel.wait_for_page_load()
        navigation_panel.go_to("Admin")

    def init_admin_page_header(self):
        admin_header = AdminHeader(self.driver)
        admin_header.go_to('Qualifications')

    def click_qualification(self):

        skills_option = self.get_wait().wait_for_element_to_be_clickable(self.SKILLS_OPTION)
        skills_option.click()

    def adding_new_skill(self):
        try:
            added_skill = self.get_wait().wait_for_element(self.SKILL_TEXT)
            added_skill.click()

        except:
            add_button = self.get_wait().wait_for_element_to_be_clickable(self.ADD_BUTTON)
            add_button.click()

            add_skill_name = self.get_wait().wait_for_element_to_be_clickable(self.ADD_NAME_FIELD)
            add_skill_name.click()
            self.clear_field(add_skill_name)
            add_skill_name.send_keys('Python')
            skill_description = self.get_wait().wait_for_element_to_be_clickable(self.ADD_DESCRIPTION_FIELD)
            skill_description.click()
            self.clear_field(skill_description)
            skill_description.send_keys(self.DESCRIPTION_TEXT)

            save_button = self.get_wait().wait_for_element_to_be_clickable(self.SAVE_BUTTON)
            save_button.click()
            added_educ = self.get_wait().wait_for_element(self.SKILL_TEXT)
            added_educ.click()
