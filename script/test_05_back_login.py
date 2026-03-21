from page.page_back_login import PageBackLogin
from script import log
from tools import DriverTools


class TestBackLogin:
    def setup_method(self):
        """前置：打开登录页"""
        driver = DriverTools.get_driver()
        self.back_login = PageBackLogin(driver)
        # 打开页面
        self.back_login.open_url()

    def teardown_method(self):
        # 截图
        self.back_login.get_shot("back_login.png")
        DriverTools.quit_driver()

    def test_01_back_login_success(self):
        """测试后台登录成功"""
        # 准备数据
        # 调用方法
        self.back_login.back_login("admin", "HM_2025_test", "8888")
        # 打印结果
        result = self.back_login.get_success_result()
        log.info(f"后台登录结果：{result}")
        # 断言
        assert "admin" in result