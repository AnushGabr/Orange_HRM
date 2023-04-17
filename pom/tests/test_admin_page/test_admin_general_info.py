import pytest

from pom.pages.admin.admin_general_info import Admin


@pytest.mark.usefixtures('log_in')
class TestAdmin:

    def test_general_admin_changes(self):
        admin = Admin(self.driver)
        admin.init_admin_page()
        admin.init_admin_page_header()
        admin.click_organization()
        admin.changing_organization_name()
        admin.changing_email()
        admin.changing_address()
        admin.changing_city()
        admin.changing_country()
        admin.fill_textarea()

        admin.saving()
        admin.wait_for_page_load()

        assert admin.check_organization_name_is_correct()
        assert admin.check_email_is_correct()
        assert admin.check_address_is_correct()
        assert admin.check_nationality_correct()
        assert admin.check_textarea()



