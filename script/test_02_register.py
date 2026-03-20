from page.page_register import PageRegister
from script import log
from tools import DriverTools


class TestLogin:

    def setup_method(self):
        """前置方法"""
        # 准备数据
        driver = DriverTools.get_driver()
        self.page_register = PageRegister(driver)
        # 调用方法
        self.page_register.open_url()

    def teardown_method(self):
        """后置方法"""
        DriverTools.quit_driver()

    def test_01_register_success(self):
        # 准备数据
        self.page_register.register("13801113018","Aa123456","8888","666666")
        # 获取结果
        result = self.page_register.get_success_result()
        log.info(f"注册结果:{result}")
        assert "注册成功" in result

    def test_02_register_fail_phone_error(self):
        # 准备数据
        self.page_register.register("13801112008","Aa123456","8888","666666")
        # 获取结果
        result = self.page_register.get_fail_result()
        log.info(f"注册结果:{result}")
        assert "注册抢88现金" in result

