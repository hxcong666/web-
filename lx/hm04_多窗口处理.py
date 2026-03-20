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
# 点击新窗口打开百度
driver.find_element(By.ID,"fw").click()
# 获取当前所有窗口的句柄
handles = driver.window_handles
print(handles)
# 切换窗口
driver.switch_to.window(handles[1])
# 新窗口搜索软件测试
driver.find_element(By.ID,"kw").send_keys("软件测试")
# 搜索操作截图
driver.get_screenshot_as_file("baidu.png")

# 5.等待2秒
time.sleep(2)
# 6.退出浏览器
driver.quit()
