

from config import *
from page.page_login import PageLogin
from page.page_open_account import PageOpenAccount
from script import log
from tools import DriverTools


class TestOpenAccount:

    def setup_method(self):
        # 创建浏览器对象
        driver = DriverTools.get_driver()
        # 创建页面对象
        self.page_login = PageLogin(driver)
        self.open_acc = PageOpenAccount(driver)
        # 打开登录页面
        self.page_login.open_url()
        # 登录成功
        self.page_login.login("17719841967","Aa123456")

    def teardown_method(self):
        # 退出
        DriverTools.quit_driver()

    def test_01_open_account_success(self):
        # 准备数据
        # self.open_acc = PageOpenAccount(DriverTools.get_driver())
        # 调用方法
        self.open_acc.open_account(NAME, CARD)
        # 打印结果
        result = self.open_acc.get_success_result()
        log.info(f"开户结果：{result}")
        # 断言
        assert "OK" in result