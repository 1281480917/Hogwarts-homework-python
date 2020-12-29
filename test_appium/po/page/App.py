from appium import webdriver

from test_appium.po.page.main_page import MainPage


class App():

    def start(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "127.0.0.1:7555"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        caps["noReset"] = "true"
        # caps["ensureWebviewsHavePages"] = True
        # # 设置页面等待空闲状态的时间
        # caps['settings[waitForIdleTimeout]'] = 0
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)
    def goto_main(self):
        return MainPage(self.driver)