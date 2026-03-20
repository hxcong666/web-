# 1.导包
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 2.打开浏览器（创建浏览器驱动对象）
path = r"C:\Program Files\Python311\chromedriver.exe"
ser = Service(executable_path=path)  # Chrome浏览器驱动服务对象
driver = webdriver.Chrome(service=ser)  # 打开Chrome浏览器
# 3.输入网址
driver.get("http://192.168.17.136/Home/user/login.html")
driver.maximize_window()
# 4.页面操作
# 4.1 登录成功
# 获取元素对象：用户名
ele = driver.find_element(by=By.ID, value="username")
# # 输入操作
ele.send_keys("13800000001")
# 获取元素对象：密码
driver.find_element(by=By.NAME, value="password").send_keys("123456")
# 获取元素对象:验证码
driver.find_element(by=By.ID, value="verify_code").send_keys("8888")
# # 点击操作
ele1 = (WebDriverWait(driver, 5).
       until(EC.visibility_of_element_located((By.CLASS_NAME, "J-login-submit"))))
ele1.click()
# driver.find_element(by=By.CLASS_NAME, value="J-login-submit").click()
# 4.2 进入账户设置
# 通过鼠标悬停，找到对应的位置： //span[text()="账户设置"]
ele2 = (WebDriverWait(driver, 5).
 until(EC.visibility_of_element_located((By.XPATH, "//span[text()='账户设置']"))))
action = ActionChains(driver)  # 创建鼠标操作对象
action.move_to_element(ele2)  # 调用鼠标悬停方法
action.perform()  # 执行鼠标操作
# 再去：点击收货地址 //a[2][text()="收货地址"]
driver.find_element(by=By.XPATH, value='//a[2][text()="收货地址"]').click()
# 点击新增收货地址
driver.find_element(by=By.CLASS_NAME, value="co_blue").click()
# 4.3 添加收货地址
driver.find_element(by=By.NAME, value="consignee").send_keys("张三")
driver.find_element(by=By.NAME, value="mobile").send_keys("13800000001")

select1 = Select(driver.find_element(by=By.ID, value="province"))
select1.select_by_value("1")

select2 = Select(driver.find_element(by=By.ID, value="city"))
select2.select_by_visible_text("市辖区")

select3 = Select(driver.find_element(by=By.ID, value="district"))
select3.select_by_index(1)
# 详细地址
driver.find_element(by=By.CSS_SELECTOR, value='[placeholder="详细地址"]').send_keys("北京胡同1号")
driver.find_element(by=By.NAME, value='zipcode').send_keys("100000")
time.sleep(1)
driver.find_element(by=By.ID, value='address_submit').click()
# 5.等待2秒
time.sleep(2)
# 6.退出浏览器
driver.quit()
