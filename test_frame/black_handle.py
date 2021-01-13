import allure,logging
from selenium.common.exceptions import NoSuchElementException


def black_a(fun):
    def run(*args,**kwargs):
        basepage=args[0]
        try:
            logging.info("start find: \nargs: " + str(args) + " kwargs: " + str(kwargs))
            return fun(*args,**kwargs)
        except NoSuchElementException as e:
            basepage.screenshot("nosuchelement.png")
            with open("./nosuchelement.png","rb") as f:
                picture_data=f.read()
            allure.attach(picture_data,attachment_type=allure.attachment_type.PNG)
            for black in basepage.black_list:
                value = basepage.driver.find_element(*black)
                if value != None:
                    value.click()
                    return fun(*args,**kwargs)
            raise e
    return run
def black_wrapper(fun):
    def run(*args, **kwargs):
        basepage = args[0]
        try:
            return fun(*args, **kwargs)
        # 捕获元素没找到异常
        except Exception as e:
            # 遍历黑名单中的元素，进行处理
            for black in basepage.black_list:
                eles = basepage.finds(*black)
                # 黑名单被找到
                if len(eles) > 0:
                    # 对黑名单元素进行点击，可以自由扩展
                    eles[0].click()
                    return fun(*args, **kwargs)
            raise e

    return run
