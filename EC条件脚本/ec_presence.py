from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
wait = WebDriverWait(driver, 10)

# 等待元素出现在 DOM 中（不管是否可见、是否可交互）
search_input = wait.until(EC.presence_of_element_located((By.ID, "kw")))
# 用 JavaScript 直接赋值，绕过 Selenium 的交互检查
driver.execute_script("arguments[0].value = 'presence测试';", search_input)
print("✅ 元素已存在于 DOM 中，已通过 JS 填入文字")

driver.quit()