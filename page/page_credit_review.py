import time

from selenium.webdriver.common.by import By
from base.base import BasePage


class PageCreditReview(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        # 主要菜单
        self.loan_manger = (By.LINK_TEXT,"借款管理")
        self.limit_manager = (By.XPATH,"//span[text()='额度管理']")
        self.app_review = (By.LINK_TEXT,"额度申请审核")
        # 搜索
        self.frame1 = (By.ID,"iframe_box")  # 进入iframe
        self.search_phone = (By.NAME,"member_name")  # 用户名
        self.search_btn = (By.CSS_SELECTOR,".srcbtn")  # 搜索按钮
        # 记录选中审核
        self.select_rec = (By.XPATH,"//tbody/tr[1]/td[2]")  # 选中第一条
        self.review_btn = (By.XPATH,"//li[1]/a/span")  # 审核按钮
        # 输入审核信息
        self.frame2 = (By.CSS_SELECTOR,"#xubox_iframe1") # 再进入另一个iframe
        self.pass_btn = (By.CSS_SELECTOR, '.ace.ng-pristine.ng-untouched.ng-valid') # 通过
        self.note = (By.CSS_SELECTOR,"tr:nth-child(6) > td:nth-child(2) > div > textarea") # 审核备注
        self.code = (By.NAME,"valicode")  # 验证码
        self.submit_btn = (By.CSS_SELECTOR,".dybtn.dybtn-save")  # 保存按钮
        # 审核记录
        self.app_rec = (By.LINK_TEXT,"额度申请记录")  # 额度申请记录
        self.status = By.CSS_SELECTOR,"select[name='status']"  # 状态
        self.rec_list = By.CSS_SELECTOR,"body > div:nth-child(2) > div.info_list > table > tbody > tr:nth-child(1) > td.status > span"  # 审核列表状态

    def menu_manager(self):
        """进入一二三级菜单"""
        self.base_click(self.loan_manger)
        self.base_click(self.limit_manager)
        self.base_click(self.app_review)

    def search_record(self,phone):
        """搜索手机号"""
        self.base_switch_frame(self.frame1)
        self.base_input(self.search_phone,phone)
        self.base_click(self.search_btn)

    def select_record(self):
        """选择第一条记录"""
        time.sleep(1)
        self.base_click(self.select_rec)
        self.base_click(self.review_btn)

    def review_commit(self,note,code):
        """审核通过"""
        self.base_switch_frame(self.frame2)
        self.base_click(self.pass_btn)
        self.base_input(self.note, note)
        self.base_input(self.code, code)
        self.base_click(self.submit_btn)

    def application_record(self,phone,status="通过"):
        """额度申请记录"""
        self.base_default_frame()  # 退出当前frame
        self.base_click(self.app_rec)
        self.base_switch_frame(self.frame1)
        self.base_input(self.search_phone, phone)
        self.base_select_list(self.status,status)
        self.base_click(self.search_btn)

    def get_success_result(self):
        """获取成功结果"""
        time.sleep(1)  # 搜索之后页面需要刷新
        result = self.fd_element(self.rec_list).text
        return result

