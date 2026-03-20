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
driver.get("http://121.43.169.97:8082/")
driver.maximize_window()
driver.implicitly_wait(5)
# 4.页面操作
WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,"username"))).send_keys("admin")
driver.find_element(By.ID,"password").send_keys("HM_2025_test")
driver.find_element(By.ID,"valicode").send_keys("8888")
driver.find_element(By.CSS_SELECTOR,".login-button").click()
# 断言
result = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"li.light-blue > a > span"))).text
print( result)
assert "admin" in result
# 5.等待2秒
time.sleep(2)
# 6.退出浏览器
driver.quit()
