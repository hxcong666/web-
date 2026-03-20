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
# 额度审核
WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//*[text()='借款管理']"))).click()
WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//*[text()='额度管理']"))).click()
# #sidebar > ul > li.ng-scope.open > ul > li:nth-child(2) > a
# //*[@id="sidebar"]/ul/li[5]/ul/li[2]/a
WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="sidebar"]/ul/li[5]/ul/li[2]/a'))).click()
# 切换frame
fr = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,"iframe_box")))
driver.switch_to.frame(fr)
driver.find_element(By.NAME,"member_name").send_keys("13800001008")
driver.find_element(By.CSS_SELECTOR,".srcbtn").click()
# 选择最近记录  //tbody/tr[1]/td[2]
time.sleep(1)
WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//tbody/tr[1]/td[2]"))).click()
# //li[1]/a/span
WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//li[1]/a/span"))).click()
# 填写审核信息
fr = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,"xubox_iframe1")))
driver.switch_to.frame(fr)
driver.find_element(By.CSS_SELECTOR,".ace.ng-pristine.ng-untouched.ng-valid").click()
driver.find_element(By.CSS_SELECTOR,"tr:nth-child(6) > td:nth-child(2) > div > textarea").send_keys("额度审核通过")
driver.find_element(By.NAME,"valicode").send_keys("8888")
driver.find_element(By.CSS_SELECTOR,".dybtn.dybtn-save").click()
# 5.等待2秒
time.sleep(2)
# 6.退出浏览器
driver.quit()
