from test_selenium.po.page.base_page import BasePage
from test_selenium.po.page.address_list_page import AddressListPage
class StartPage(BasePage):
    '''
    导航页
    '''
    def goto_address(self):
        '''
        跳转到通讯录页面
        :return:
        '''
        self.driver.find_element_by_css_selector('#menu_contacts').click()
        return AddressListPage(self.driver)
