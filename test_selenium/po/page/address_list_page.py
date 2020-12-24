from test_selenium.po.page.base_page import BasePage
from test_selenium.po.page.add_member_page import AddMemberPage
from selenium.common.exceptions import NoSuchElementException
class AddressListPage(BasePage):
    def goto_add_member(self):
        '''
        跳转到添加成员页面
        :return:
        '''
        self.driver.find_element_by_css_selector('#js_contacts47 > div > div.member_colLeft > div > div.member_colLeft_top.member_colLeft_top_BorderBottom > a').click()
        return AddMemberPage(self.driver)
    def get_departments(self,depatments):
        '''
        获得部门信息
        :return:
        '''
        self.driver.find_element_by_xpath('//*[@id="memberSearchInput"]').send_keys(depatments)
        try:
            result=self.driver.find_element_by_xpath('//*[@id="search_party_list"]/li/a').text
        except NoSuchElementException as e:
            result=''
        return result
if __name__ == '__main__':
    AddressListPage().get_departments('a')