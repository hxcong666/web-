# 类三要素
# 1.定义页面类
# 2.设置实例属性
# 3.定义实例方法
import time
from base.base import BasePage
from config import BASE_URL
from tools import DriverTools
from selenium.webdriver.common.by import By


class PageLogin(BasePage):
    """登录页面类"""

    def __init__(self, driver):
        """初始化方法"""
        # 获取driver对象
        # driver = DriverTools.get_driver()
        super().__init__(driver)
        # 设置页面实例属性
        self.username = (By.ID,"keywords")
        self.password = (By.ID,"password")
        self.login_button = (By.ID,"login-btn")
        # 成功结果元素属性
        self.success_result = (By.CLASS_NAME,"a-link1")
        # 失败结果元素属性 #err > span
        self.fail_result = (By.CSS_SELECTOR,"#err")

    def open_url(self):
        """打开网页"""
        self.driver.get(BASE_URL + "/common/member/login")

    def login(self, username, password):
        """登录"""
        # 输入账号
        self.base_input(self.username, username)
        # 输入密码
        self.base_input(self.password, password)
        # 点击登录
        self.base_click(self.login_button)
        time.sleep(2)

    def get_success_result(self):
        """获取成功结果"""
        return self.fd_element(self.success_result).text

    def get_fail_result(self):
        """获取失败结果"""
        return self.fd_element(self.fail_result).text


if __name__ == '__main__':
    # 创建对象
    lg = PageLogin(DriverTools.get_driver())
    # 打开页面
    lg.open_url()
    # 操作登录
    lg.login("13800001001","Aa123456")
