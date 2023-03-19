from selenium.webdriver.common.by import By

from pom.base.base_page import BasePage


class AdminHeader(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    ROOT_ELEMENT = (By.CSS_SELECTOR, '.oxd-topbar-body-nav')
    HEADER_ITEMS = (By.CSS_SELECTOR, '.oxd-topbar-body-nav li')

    def get_header_items(self):
        self.get_wait().wait_for_page()
        header_elements = self.get_wait().wait_for_list_size_change(self.HEADER_ITEMS, size=7)
        header_item_names = ["User Management", 'Job', 'Organization', 'Qualifications', 'Nationalities', 'Corporate Branding', 'Configuration']
        return dict(zip(header_item_names, header_elements))

    def go_to(self, page):
        element = self.get_header_items().get(page)
        self.get_wait().wait_for_element_to_be_clickable(element)
        self.click(element)