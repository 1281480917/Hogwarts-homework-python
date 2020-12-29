from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait

from test_appium.po.page.BasePage import BasePage


class ContactAdd(BasePage):
    """
    成员信息编辑
    """

    def add_contact(self):
        """
        添加信息
        :return:
        """
        self.send(MobileBy.XPATH, "//*[contains(@text,'姓名')]/..//*[@text='必填']",'aaa')
        #self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'姓名')]/..//*[@text='必填']").send_keys('aaa')
        self.find_and_click(MobileBy.XPATH, "//*[contains(@text,'性别')]/..//*[@text='男']")
        WebDriverWait(self.driver, 10).until(lambda driver: self.driver.find_element(MobileBy.XPATH, "//*[@text='女']"))
        self.find_and_click(MobileBy.XPATH, "//*[@text='女']")
        self.send(MobileBy.XPATH, "//*[contains(@text,'手机')]/..//*[@text='手机号']", '11114444999')
        #self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'手机')]/..//*[@text='手机号']").send_keys(
            #'11114444999')
        self.find_and_click(MobileBy.XPATH, "//*[@text='保存']")
        return True
