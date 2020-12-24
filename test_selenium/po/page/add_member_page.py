from test_selenium.po.page.base_page import BasePage
from test_selenium.po.page.add_departments_page import AddDepartmentsPage
class AddMemberPage(BasePage):
    def goto_add_departments(self):
        '''
        添加部门
        :return:
        '''
        self.driver.find_element_by_css_selector('#js_contacts47 > div > div.member_colLeft > ul > li:nth-child(1) > a').click()
        return AddDepartmentsPage(self.driver)
