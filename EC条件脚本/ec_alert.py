from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
wait = WebDriverWait(driver, 5)

# 百度首页没有 alert，5 秒后必定超时（预期行为）
try:
    alert = wait.until(EC.alert_is_present())
    print("✅ 弹窗出现了（实际上不会执行）")
except:
    print("⏰ 超时，没有弹窗出现（符合预期）")

driver.quit()