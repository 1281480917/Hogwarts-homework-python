from test_selenium.po.page.base_page import BasePage

class AddDepartmentsPage(BasePage):
    def add_departments(self,depatments):
        '''
        添加部门
        :return:
        '''
        from test_selenium.po.page.address_list_page import AddressListPage
        self.driver.find_element_by_xpath("//*[@name='name']").send_keys(depatments)
        self.driver.find_element_by_css_selector('.js_toggle_party_list').click()
        self.driver.find_element_by_css_selector(".qui_dialog_body.ww_dialog_body [id='1688850455595574_anchor']").click()
        self.driver.find_element_by_css_selector(
            "#__dialog__MNDialog__ > div > div.qui_dialog_foot.ww_dialog_foot > a.qui_btn.ww_btn.ww_btn_Blue").click()
        return AddressListPage(self.driver)