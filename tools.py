import json
import logging
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from logging import handlers

from webdriver_manager.chrome import ChromeDriverManager

from config import PATH


class DriverTools:
    """浏览器驱动类"""

    # 类属性
    driver = None

    @classmethod
    def get_driver(cls):
        """获取浏览器驱动"""
        if cls.driver is None:
            options = Options()

            # 判断是否在 GitHub Actions 服务器环境中运行
            if os.environ.get('GITHUB_ACTIONS') == 'true':
                # --- 服务器环境 (Linux) ---
                # 添加无头模式及相关必须参数
                options.add_argument('--headless')
                options.add_argument('--no-sandbox')
                options.add_argument('--disable-dev-shm-usage')

                # 【新增这一行】强制指定窗口大小，防止页面元素因为窗口太小被折叠或遮挡
                options.add_argument('--window-size=1920,1080')
                # 自动下载并配置对应版本的驱动
                ser = Service(executable_path=ChromeDriverManager().install())
            else:
                # --- 本地电脑环境 (Windows) ---
                # 本地使用你指定的本地驱动路径，且不开启 headless（可以看到界面）
                path = r"D:/chromedriver-win64/chromedriver.exe"
                ser = Service(executable_path=path)

            # 打开 Chrome 浏览器
            cls.driver = webdriver.Chrome(service=ser, options=options)

            # 浏览器最大化
            cls.driver.maximize_window()
            cls.driver.implicitly_wait(10)

        # 返回浏览器驱动对象
        return cls.driver

    @classmethod
    def quit_driver(cls):
        """退出浏览器驱动"""
        if cls.driver:
            # 等待2秒
            time.sleep(2)
            # 退出浏览器
            cls.driver.quit()
            # 置空
            cls.driver = None


def read_json(file_name):
    """
    读取JSON文件并转换为格式为 [(), (), ...] 的列表
    :param file_name: json文件名
    :return: 列表
    """
    data = []
    file_path = PATH + "/data/" + file_name
    with open(file_path, mode='r', encoding='utf-8') as f:
        # 读取JSON文件并解析为Python对象
        tmp = json.load(f)
        for i in tmp:
            a = tuple(i.values())
            data.append(a)
        # 返回列表
        return data


class GetLog:
    # 日志器
    __log = None

    @classmethod
    def get_log(cls):
        if cls.__log is None:
            # 获取日志器
            cls.__log = logging.getLogger()
            # 设置入口级别
            cls.__log.setLevel(logging.INFO)
            # 获取处理器
            filename = PATH + "/log/" + "web.log"
            tf = logging.handlers.TimedRotatingFileHandler(filename=filename,  # 日志文件名
                                                           when="midnight",  # 日志归档时间
                                                           interval=1,  # 每天归档一次
                                                           backupCount=3,  # 保留3天日志
                                                           encoding="utf-8")  # 日志编码格式
            # 获取格式器
            fmt = "%(asctime)s %(levelname)s [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s"
            fm = logging.Formatter(fmt)
            # 将格式器添加到处理器
            tf.setFormatter(fm)
            # 将处理器添加到日志器
            cls.__log.addHandler(tf)
        # 返回日志器
        return cls.__log


if __name__ == '__main__':
    print(read_json("login_data.json"))
