from appium.webdriver.common.mobileby import MobileBy

from test_appium.po.page.BasePage import BasePage
from test_appium.po.page.member_invite_menu_page import MemberInviteMenuPage


class AddressListPage(BasePage):
    def click_addmember(self):
        # self.driver.find_element(MobileBy.
        #                          ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().'
        #                                               'scrollable(true).instance(0)).'
        #                                               'scrollIntoView(new UiSelector().'
        #                                               'text("添加成员").instance(0));').click()
        self.swip(MobileBy.XPATH, "//*[@text='添加成员']").click()
        return MemberInviteMenuPage(self.driver)