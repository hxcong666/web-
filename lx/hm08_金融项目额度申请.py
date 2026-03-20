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
# 点击账户切换
WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//em[text()='借款账户']"))).click()
WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.LINK_TEXT,'申请额度'))).click()
# 填写信息
WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,"amount_account"))).send_keys("100")
driver.find_element(By.NAME,"remark").send_keys("额度申请测试")
driver.find_element(By.ID,"verifycode").send_keys("8888")
driver.find_element(By.CSS_SELECTOR,".btn-submit.btn-md").click()
time.sleep(2) # #amount_list > tr:nth-child(1) > td:nth-child(3)
result = (WebDriverWait(driver,10).
          until(EC.visibility_of_element_located((By.CSS_SELECTOR,"#amount_list> tr.ng-scope > td:nth-child(3)"))).text)

# 断言
# result = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"body"))).text
print(result)
assert "100.00" == result

# 5.等待2秒
time.sleep(2)
# 6.退出浏览器
driver.quit()
