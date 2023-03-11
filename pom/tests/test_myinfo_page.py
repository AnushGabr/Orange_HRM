import pytest
from pom.pages.login import LoginPage
from pom.pages.navigation_panel import NavigationPanel
from pom.pages.my_info_page import MyInfoPage


@pytest.mark.usefixtures('log_in')
class TestMyInfo:

    def test_basic_inputs(self):
        my_info = MyInfoPage(self.driver)
        my_info.init_my_info_page()
        my_info.first_input_field()
        assert my_info.is_first_input_field_valid()
