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
driver.get("http://121.43.169.97:8081/")
driver.maximize_window()
# 4.页面操作
# ①点击注册按钮
driver.find_element(By.LINK_TEXT,"有奖注册").click()
# ②填写注册信息
driver.find_element(By.ID,"phone").send_keys("13800001008")
driver.find_element(By.ID,"password").send_keys("Aa123456")
driver.find_element(By.ID,"verifycode").send_keys("8888")
driver.find_element(By.ID,"get_phone_code").click()
time.sleep(2)
driver.find_element(By.ID,"phone_code").send_keys("666666")
driver.find_element(By.CLASS_NAME,"lg-btn").click()
# 断言
time.sleep(2)
result = driver.find_element(By.CSS_SELECTOR,"div.reg-step-last > h1").text
print(result)
assert "注册成功" in result
# 5.等待2秒
time.sleep(2)
# 6.退出浏览器
driver.quit()
