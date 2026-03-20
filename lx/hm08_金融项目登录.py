# 1.导包
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 2.打开浏览器（创建浏览器驱动对象）
path = r"C:\Program Files\Python311\chromedriver.exe"
ser = Service(executable_path=path)  # Chrome浏览器驱动服务对象
driver = webdriver.Chrome(service=ser)  # 打开Chrome浏览器
# 3.输入网址
driver.get("http://121.43.169.97:8081/")
driver.maximize_window()
# 4.页面操作
# ①点击注册按钮
driver.find_element(By.LINK_TEXT,"登录").click()
# ②填写注册信息
driver.find_element(By.ID,"keywords").send_keys("13800001008")  # 不重复
driver.find_element(By.ID,"password").send_keys("Aa123456")
driver.find_element(By.ID,"login-btn").click()
# time.sleep(2)
# 点击开通资金托管
ele1 = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.LINK_TEXT,"立即开通")))
ele1.click()
# 填写姓名和身份证信息
ele2 = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.NAME,"realname")))
ele2.send_keys("张三四")
driver.find_element(By.NAME,"card_id").send_keys("110101199607284822")  # 不重复
# 点击提交
time.sleep(1)
driver.find_element(By.CSS_SELECTOR,'[value="确认提交"]').click()
# 点击立即开通
ele3 = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,".btn.ng-scope")))
ele3.click()
# 断言  body  /html/body
time.sleep(1)
# 切换新窗口
handles = driver.window_handles
driver.switch_to.window(handles[1])
ele4 = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"body")))
result = ele4.text
print(result)
assert "OK" in result
driver.close()
# 返回上级窗口
time.sleep(1)
driver.switch_to.window(handles[0])
driver.find_element(By.CLASS_NAME,"closeWinow").click()

# 5.等待2秒
time.sleep(2)
# 6.退出浏览器
driver.quit()
