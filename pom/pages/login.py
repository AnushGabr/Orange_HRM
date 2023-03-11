from selenium.webdriver.common.by import By
from pom.base.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    USERNAME_FIELD = (By.CSS_SELECTOR, 'input[name="username"]')
    PASSWORD_FIELD = (By.CSS_SELECTOR, 'input[name="password"]')
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'button[type="submit"]')
    INVALID_CREDENTIALS_ALERT = (By.CSS_SELECTOR, 'div[class="oxd-alert oxd-alert--error"]')

    def fill_username_field(self, username):
        element = self.get_wait().wait_for_element(self.USERNAME_FIELD)
        element.send_keys(username)

    def fill_password_field(self, password):
        self.find_element_by(self.PASSWORD_FIELD).send_keys(password)

    def click_login(self):
        self.find_element_by(self.LOGIN_BUTTON).click()

    def login(self, username, password):
        self.fill_username_field(username)
        self.fill_password_field(password)
        self.click_login()

    def is_invalid_credential_alert_visible(self):
        return self.get_wait().wait_for_element(self.INVALID_CREDENTIALS_ALERT)
