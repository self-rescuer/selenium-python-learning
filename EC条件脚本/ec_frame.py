from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
wait = WebDriverWait(driver, 5)

# 百度首页没有 frame，5 秒后必定超时（预期行为）
try:
    wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, "nonexistent_frame")))
    print("✅ 已切换到 frame（实际上不会执行）")
except:
    print("⏰ 超时，没有找到 frame（符合预期）")

driver.quit()