import pytest
from pom.base.webdriver_factory import WebDriverFactory
from pom.pages.login import LoginPage


@pytest.fixture
def set_up(request):
    web_driver_factory = WebDriverFactory(request.config.getoption("--browser"))
    driver = web_driver_factory.get_web_driver_instance()
    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    driver.quit()


@pytest.fixture
def log_in(request, set_up):
    login_page = LoginPage(request.cls.driver)
    login_page.login("Admin", "admin123")


def pytest_addoption(parser):
    parser.addoption("--browser")