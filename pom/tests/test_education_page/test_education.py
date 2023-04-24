import pytest
from pom.pages.qualifications.education import Education
@pytest.mark.usefixtures('log_in')

class TestEducation:

    def test_education_page(self):
        education = Education(self.driver)
        education.init_admin_page()
        education.init_admin_page_header()
        education.click_qualification()
        education.adding_new_education()


