from selenium import webdriver


class WebDriverFactory:

    def __init__(self, browser_type):
        self.browser_type = browser_type

    def get_web_driver_instance(self):

        URL = "https://opensource-demo.orangehrmlive.com"
        if self.browser_type == 'firefox':
            driver = webdriver.Firefox()
        elif self.browser_type == 'edge':
            driver = webdriver.Edge()
        else:
            driver = webdriver.Chrome()

        driver.get(URL)
        return driver
