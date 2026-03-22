import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from page.page_login import PageLogin
from page.page_open_account import PageOpenAccount


# 编写浏览器驱动创建退出
@pytest.fixture()
def browser():
    # 创建浏览器驱动对象
    path = r"D:/chromedriver-win64/chromedriver.exe"
    ser = Service(executable_path=path)  # Chrome浏览器驱动服务对象
    driver = webdriver.Chrome(service=ser)  # 打开Chrome浏览器
    # 浏览器最大化
    driver.maximize_window()
    driver.implicitly_wait(10)
    # 返回驱动对象
    yield driver
    driver.quit()


@pytest.fixture()
def a_login(browser):
    """登录页面对象"""
    page_login = PageLogin(browser)
    # 打开登录页面
    page_login.open_url()
    # 返回登录页面对象
    return page_login

@pytest.fixture()
def b_login(browser):
    """登录页面对象"""
    page_login = PageLogin(browser)
    open_acc = PageOpenAccount(browser)
    # 打开登录页面
    page_login.open_url()

    page_login.login("17719841965", "Aa123456")

    # 返回登录页面对象
    return open_acc