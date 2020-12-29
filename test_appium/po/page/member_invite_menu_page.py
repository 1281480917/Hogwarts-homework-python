from appium.webdriver.common.mobileby import MobileBy

from test_appium.po.page.BasePage import BasePage
from test_appium.po.page.contact_add import ContactAdd


class MemberInviteMenuPage(BasePage):
    """
    添加成员 PO
    """
    def add_member_manual(self):
        self.find_and_click(MobileBy.XPATH, "//*[@text='手动输入添加']")
        return ContactAdd(self.driver)
