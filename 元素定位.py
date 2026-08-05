from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge(service=Service(r"D:\自动化测试\msedgedriver.exe"))
driver.get("https://www.baidu.com")
time.sleep(2)

# 用你看到的 id 定位输入框
search_input = driver.find_element(By.ID, "chat-textarea")
search_input.send_keys("Selenium")

# 按回车键搜索（因为不知道"百度一下"按钮的 id 是什么）
search_input.send_keys("\n")

time.sleep(3)
driver.quit()