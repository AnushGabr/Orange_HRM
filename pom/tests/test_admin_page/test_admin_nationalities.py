import pytest
from pom.pages.admin.admin_general_info import Admin
from pom.pages.admin.admin_nationalities import Nationalities

@pytest.mark.usefixtures("log_in")
class TestNationalities:
    def test_admin_nationalities(self):
        admin = Admin(self.driver)
        admin.init_admin_page()
        nationalities = Nationalities(self.driver)
        nationalities.init_admin_page_nationalities()
        nationalities.add_nationality("Median")
        assert nationalities.is_record_number_updated(), "Record number has not been updated."
        assert nationalities.is_nationality_present("Median"), "Nationality 'Median' is not found in the lists."
        nationalities.edit_nationality_name("Mexican", "Latin")
        assert nationalities.is_edit_nationality_success_message_displayed(), "No edited success message."
        assert nationalities.is_nationality_present("Latin"), "Nationality 'Latin' is not found in the lists."
        nationalities.delete_nationality("Median")
        assert nationalities.is_delete_nationality_success_message_displayed(), "No delete success message"
        nationalities.select_checkboxes("Irish")
        assert nationalities.is_nationality_selected("Irish")

# test data should be changed before running the tests second time
# test cases above cover pretty much most of the things on the page
