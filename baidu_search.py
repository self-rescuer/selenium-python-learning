from selenium import webdriver
from selenium.webdriver.edge.service import Service
import time

# 1. 指定Edge驱动的路径（改成你自己的路径）


# 2. 启动Edge浏览器
driver = webdriver.Edge(service = Service(r"D:\自动化测试\msedgedriver.exe"))

# 3. 打开百度首页
driver.get("https://www.baidu.com")

# 4. 等待3秒，让你看到浏览器确实打开了
time.sleep(3)

# 5. 关闭浏览器
driver.quit()
