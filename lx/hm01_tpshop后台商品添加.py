# 1.导包
import time
from selenium import webdriver
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
driver.get("http://192.168.17.136/admin")
# 全局的等待：隐式等待
driver.implicitly_wait(10)
driver.maximize_window()  # 浏览器最大化
# 4.页面操作
# 4.1 登录
driver.find_element(By.NAME,"username").send_keys("admin")
driver.find_element(By.NAME,"password").send_keys("123456")
driver.find_element(By.ID,"vertify").send_keys("8888")
driver.find_element(By.NAME,"submit").click()
# 4.2 点击商城
# time.sleep(1)
# driver.find_element(By.LINK_TEXT,"商城").click()
ele = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.LINK_TEXT,"商城")))
ele.click()
# 4.3 点击添加商品
# time.sleep(1)
# 切换frame
fr = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,"workspace")))
# fr = driver.find_element(By.ID,"workspace")
driver.switch_to.frame(fr)
# 点击添加商品
driver.find_element(By.XPATH,"//*[text()='添加商品']").click()
# # 返回原来页面（从frame中出来）
# driver.switch_to.default_content()
# 填写商品信息
# 商品名称
driver.find_element(By.NAME,"goods_name").send_keys("测试商品test04")
# 选择种类
select1 = Select(driver.find_element(By.ID,"cat_id"))
select1.select_by_value("31")  # value属性值

select2 = Select(driver.find_element(By.ID,"cat_id_2"))
select2.select_by_visible_text("运营商")  # 文本

select3 = Select(driver.find_element(By.ID,"cat_id_3"))
select3.select_by_index(1)  # 下标
# 填写商品价格
time.sleep(1)
driver.find_element(By.NAME,"shop_price").send_keys("99")
driver.find_element(By.NAME,"market_price").send_keys("99")
# 是否包邮
time.sleep(1)
driver.find_element(By.ID,"is_free_shipping_label_1").click()
# 确认提交
time.sleep(1)
driver.find_element(By.ID,"submit").click()

# 5.等待2秒
time.sleep(2)
# 6.退出浏览器
driver.quit()
