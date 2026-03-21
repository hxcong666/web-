from page.page_back_login import PageBackLogin
from page.page_credit_review import PageCreditReview
from script import log
from tools import DriverTools


class TestCreditReview:
    def setup_method(self):
        # 创建对象
        driver = DriverTools.get_driver()
        self.back_login = PageBackLogin(driver)
        # 打开登录页并登录成功
        self.back_login.open_url()
        self.back_login.back_login("admin","HM_2025_test","8888")
        # 进入菜单管理
        self.credit_rev = PageCreditReview(driver)
        self.credit_rev.menu_manager()
        # 搜索，选中最近一条记录
        self.credit_rev.search_record("17719841967")
        # 审核信息操作
        self.credit_rev.select_record()

    def teardown_method(self):
        """后置方法：截图并退出浏览器"""
        self.credit_rev.get_shot("credit_review_success.png")
        DriverTools.quit_driver()

    def test_01_credit_review_success(self):
        # 调用审核方法
        self.credit_rev.review_commit("审核通过","8888")
        # 打印结果
        self.credit_rev.application_record("17719841966")
        result = self.credit_rev.get_success_result()
        log.info(f"额度审核结果：{result}")
        # 断言
        assert "通过" == result





