import time

from selenium.webdriver.common.by import By

from base.base import BasePage
from config import BASE_URL
from tools import DriverTools


class PageRegister(BasePage):
    """登录页面类"""

    def __init__(self, driver):
        """初始化方法"""
        # 获取driver对象
        # driver = DriverTools.get_driver()
        super().__init__(driver)
        # 设置页面实例属性
        self.phone = (By.ID,"phone")
        self.password = (By.ID,"password")
        self.verifycode = (By.ID,"verifycode")
        self.get_phone_code = (By.ID,"get_phone_code")
        self.phone_code = (By.ID,"phone_code")
        self.register_button = (By.CLASS_NAME,"lg-btn")
        # 成功结果元素属性
        self.success_result = (By.CLASS_NAME,"reg-step-last")
        # 失败结果元素属性 #err > span
        self.fail_result = (By.CSS_SELECTOR,"#reg_form > div.reg-title")


    def open_url(self):
        """打开网页"""
        self.driver.get(BASE_URL + "/common/member/reg")

    def register(self, phone, password, verifycode ,phone_code):
        """登录"""
        # 输入账号
        self.base_input(self.phone , phone)
        # 输入密码
        self.base_input(self.password, password)
        # 输入验证码
        self.base_input(self.verifycode, verifycode)
        # 点击获取手机验证码
        self.base_click(self.get_phone_code)
        time.sleep(2)
        # 输入手机验证码
        self.base_input(self.phone_code, phone_code)
        # 点击免费注册
        self.base_click(self.register_button)
        time.sleep(2)

    def get_success_result(self):
        """获取成功结果"""
        return self.fd_element(self.success_result).text
    def get_fail_result(self):
        """获取失败结果"""
        return self.fd_element(self.fail_result).text

if __name__ == '__main__':
    # 创建对象
    lg = PageRegister(DriverTools.get_driver())
    # 打开页面
    lg.open_url()
    # 操作登录
    lg.register("13801112008","Aa123456","8888","666666")
    # 获取成功结果
    # result = lg.base_text(lg.success_result)
    # print(f"登录结果:{result}")
    # 断言
    # assert "13800001001" == result