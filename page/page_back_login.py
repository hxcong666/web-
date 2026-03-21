from selenium.webdriver.common.by import By
from base.base import BasePage
from config import BACK_URL


class PageBackLogin(BasePage):

    def __init__(self, driver):
        # 扩展重写父类方法
        super().__init__(driver)
        # 元素属性
        self.username = (By.ID,"username")
        self.password = (By.ID,"password")
        self.code = (By.ID,"valicode")
        self.login_button = (By.CSS_SELECTOR,".login-button")
        # 登录结果元素:admin信息
        self.success_result = (By.CSS_SELECTOR,"li.light-blue > a > span")

    def open_url(self):
        """打开后台登录页面"""
        self.driver.get(BACK_URL)

    def back_login(self, username, password, code):
        """后台登录"""
        self.base_input(self.username, username)
        self.base_input(self.password, password)
        self.base_input(self.code, code)
        self.base_click(self.login_button)

    def get_success_result(self):
        """获取登录成功结果"""
        return self.fd_element(self.success_result).text

