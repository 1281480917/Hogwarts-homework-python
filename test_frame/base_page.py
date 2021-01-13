import logging

import yaml
from appium.webdriver import WebElement
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from test_frame.black_handle import black_wrapper, black_a


class BasePage:

    def __init__(self, driver: WebDriver = None):
        self.driver = driver
        # 参考：黑名单类
        self.black_list = [(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/iv_close']")]

    # 设计模式：代理模式，装饰器模式
    # 装饰器
    @black_a
    def find(self, by, locator):
        return self.driver.find_element(by, locator)


    def finds(self, by, locator):
        return self.driver.find_elements(by, locator)

    def find_and_click(self, by, locator):
        self.find(by, locator).click()

    def find_by_scroll(self, text):
        return self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                        f'new UiScrollable(new UiSelector()\
                                 .scrollable(true).instance(0))\
                                 .scrollIntoView(new UiSelector()\
                                 .text("{text}").instance(0));')

    def find_by_swip(self, driver, by, locator):
        self.driver.implicitly_wait(1)
        elements = self.driver.find_elements(by, locator)
        while len(elements) == 0:
            self.driver.swipe(0, 0, 0, 20)
            elements = self.driver.find_elements(by, locator)
        self.driver.implicitly_wait(5)

    @staticmethod
    def find_by_swip2(driver: WebDriver, by, locator) -> WebElement:
        driver.implicitly_wait(1)
        elements = driver.find_elements(by, locator)
        while len(elements) == 0:
            driver.swipe(0, 600, 0, 400)
            elements = driver.find_elements(by, locator)
        driver.implicitly_wait(5)
        return elements[0]

    def screenshot(self, picture_path):
        self.driver.save_screenshot(picture_path)
    def get_toast_text(self):
        result = self.find(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        logging.info(result)
        return result
    def send(self, by, locator, content):
        self.find(by, locator).send_keys(content)
    def load(self,yaml_path):
        with open(yaml_path,'r',encoding='utf-8') as f:
            data=yaml.load(f)
        print(data)
        for step in data:
            find=step['find']
            action=step['action']
            by=eval(step['by'])
            print(by)
            if action=='find_and_click':
                self.find_and_click(by,find)
            elif action=='send':
                content=step['content']
                self.send(by,find,content)
if __name__ == '__main__':
    BasePage().load('page/search.yaml')