from selenium.webdriver.common.by import By
from base.base import BasePage


class PageCreditApplication(BasePage):
    """额度申请页面"""

    def __init__(self,driver):
        """设置属性"""
        super().__init__(driver)
        # 页面元素定位信息
        self.role = (By.XPATH, "//em[text()='借款账户']")
        self.application = (By.LINK_TEXT, "申请额度")
        self.money = (By.ID, "amount_account")
        self.detail = (By.NAME, "remark")
        self.code = (By.ID, "verifycode")
        self.submit = (By.CSS_SELECTOR, ".btn-submit.btn-md")
        # amount_list > tr > td:nth-child(3)
        # 提交成功结果 #amount_list > tr:nth-child(1) > td:nth-child(3)
        self.success_result = (By.CSS_SELECTOR, "#amount_list> tr.ng-scope > td:nth-child(3)")
    def switch_role(self):
        """点击切换账户"""
        self.base_click(self.role)

    def click_application(self):
        """点击额度申请"""
        self.base_click(self.application)

    def credit_application(self,money, detail, code):
        """
        额度申请提交
        :param money: 金额
        :param detail: 详情
        :param code: 验证码
        :return: 无
        """
        # 输入信息
        self.base_input(self.money, money)
        self.base_input(self.detail, detail)
        self.base_input(self.code, code)
        # 点击提交
        self.base_click(self.submit)

    def get_success_result(self):
        """获取提交成功结果"""
        return self.fd_element(self.success_result).text