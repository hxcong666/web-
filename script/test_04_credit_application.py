import time
from page.page_credit_application import PageCreditApplication
from page.page_login import PageLogin
from script import log
from tools import DriverTools


class TestCreditApplication:

    def setup_method(self):
        # 准备数据
        driver = DriverTools.get_driver()
        self.page_credit = PageCreditApplication(driver)
        self.page_login = PageLogin(driver)
        # 打开网页
        self.page_login.open_url()
        # 登录成功
        self.page_login.login("17719841966","Aa123456")


    def teardown_method(self):
        DriverTools.quit_driver()

    def test_01_credit_application_success(self):
        # 切换账户
        self.page_credit.switch_role()
        # 点击额度申请
        self.page_credit.click_application()
        # 调用方法
        self.page_credit.credit_application("10000","测试额度","8888")
        # 打印日志
        time.sleep(2)
        result = self.page_credit.get_success_result()
        log.info(f"额度申请:{result}")
        # 断言
        assert "10,000.00" == result