# 1.导包
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# 2.打开浏览器（创建浏览器驱动对象）
path = r"C:\Program Files\Python311\chromedriver.exe"
ser = Service(executable_path=path)  # Chrome浏览器驱动服务对象
driver = webdriver.Chrome(service=ser)  # 打开Chrome浏览器
# 3.输入网址
driver.get("http://121.43.169.97:8848/pageA.html")
# 4.页面操作
driver.find_element(By.LINK_TEXT, "百度").click()
# 浏览器按钮
driver.refresh()  # 刷新
driver.back()  # 后台
driver.forward()  # 前进
# 5.等待2秒
time.sleep(2)
# 6.退出浏览器
driver.quit()
