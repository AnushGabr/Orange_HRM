import pytest

from pom.pages.my_info_page import MyInfoPage


@pytest.mark.usefixtures('log_in')
class TestMyInfo:

    def test_basic_inputs(self):
        my_info = MyInfoPage(self.driver)
        my_info.init_my_info_page()
        my_info.fill_first_username_field()
        my_info.fill_midname_input_field()
        my_info.select_date()
        my_info.choose_nationality()
        my_info.select_marital_status_field()
        # my_info.gender_field()
        my_info.save_all_fields_info()

        my_info.wait_for_page_load()
        assert my_info.is_first_input_field_valid()
        assert my_info.is_midname_input_field_valid()
        assert my_info.is_selected_date_correct()
        assert my_info.is_nationality_field_correct()
        assert my_info.is_marital_status_correct()
        # assert my_info.gender_field_correct()
