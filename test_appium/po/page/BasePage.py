from appium.webdriver.webdriver import WebDriver


class BasePage():
    def __init__(self,driver: WebDriver=None):
        self.driver=driver
    def find(self,by,value):
        return self.driver.find_element(by,value)

    def find_and_click(self, by, locator):
        self.find(by, locator).click()
    def swip(self,by,value):
        self.driver.implicitly_wait(1)
        ele=self.driver.find_elements(by,value)
        while len(ele)==0:
            self.driver.swipe(0,600,0,400)
            ele=self.driver.find_elements(by,value)
        self.driver.implicitly_wait(5)
        return ele[0]
    def send(self,by, locator, text):
         self.find(by, locator).send_keys(text)