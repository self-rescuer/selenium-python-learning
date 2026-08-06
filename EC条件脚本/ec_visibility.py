from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.bing.com")  # 换为必应
wait = WebDriverWait(driver, 10)

search_input = wait.until(EC.visibility_of_element_located((By.ID, "sb_form_q")))  # 必应输入框 id
driver.execute_script("arguments[0].value = 'visibility测试';", search_input)
print("✅ 元素已可见，已通过 JS 填入文字")

driver.quit()