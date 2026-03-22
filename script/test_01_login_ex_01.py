import pytest

from page.page_login import PageLogin
from script import log
from tools import DriverTools, read_json


class TestLogin:

    # def setup_method(self):
    #     """前置方法"""
    #     # 准备数据
    #     driver = DriverTools.get_driver()
    #     self.page_login = PageLogin(driver)
    #     # 调用方法
    #     self.page_login.open_url()
    #
    # def teardown_method(self):
    #     """后置方法"""
    #     DriverTools.quit_driver()

    @pytest.mark.parametrize("phone,password,expect", read_json("login_data.json"))
    def test_01_login_success(self, a_login,phone, password,expect):
        # 准备数据
        # 调用方法
        a_login.login(phone, password)
        # 打印日志
        # result = self.page_login.get_success_result()
        # 根据期望结果判断获取成功还是失败结果
        if expect == "13800001001":
            result = a_login.get_success_result()
        else:
            result = a_login.get_fail_result()
        # print(f"登录结果:{result}")
        log.info(f"登录结果:{result}")
        # 断言
        assert expect in result