import pytest
from pom.pages.qualifications.memberships import Memberships
@pytest.mark.usefixtures('log_in')

class TestMemberships:

    def test_memberships_page(self):
        memberships = Memberships(self.driver)
        memberships.init_admin_page()
        memberships.init_admin_page_header()
        memberships.click_qualification()
        memberships.adding_new_membership()