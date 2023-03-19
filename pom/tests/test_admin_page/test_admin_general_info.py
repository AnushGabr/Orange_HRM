import pytest

from pom.pages.admin.admin_general_info import Admin


@pytest.mark.usefixtures('log_in')
class TestAdmin:

    def test_admin_color_changes(self):
        admin = Admin(self.driver)
        admin.init_admin_page()
        admin.init_admin_page_header()
        admin.click_organization()
        admin.changing_organization_name()
