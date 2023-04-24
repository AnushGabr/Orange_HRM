import pytest
from pom.pages.qualifications.skills import Skills
@pytest.mark.usefixtures('log_in')

class TestSkills:

    def test_skills_page(self):
        skills = Skills(self.driver)
        skills.init_admin_page()
        skills.init_admin_page_header()
        skills.click_qualification()
        skills.adding_new_skill()