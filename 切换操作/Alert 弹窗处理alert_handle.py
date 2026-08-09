from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.selenium.dev/selenium/web/alerts.html")

# 点击触发 Alert
driver.find_element(By.LINK_TEXT, "click me").click()
time.sleep(1)

# 切换到弹窗并处理
alert = driver.switch_to.alert
print(f"Alert 文本: {alert.text}")
alert.accept()

time.sleep(2)
driver.quit()