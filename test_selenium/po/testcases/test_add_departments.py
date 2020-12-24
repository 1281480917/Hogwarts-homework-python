from test_selenium.po.page.start_page import StartPage
import pytest
class TestAddDepartments():
    def setup_class(self):
        self.start=StartPage()

    @pytest.mark.parametrize("departments",
                             [("dsd"),])
    def test_add_departments(self,departments):
        result=self.start.goto_address().goto_add_member().goto_add_departments().add_departments(departments).get_departments(departments)
        assert result==departments