from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.bing.com")
wait = WebDriverWait(driver, 10)

search_input = wait.until(EC.element_to_be_clickable((By.ID, "sb_form_q")))
driver.execute_script("arguments[0].value = 'clickable测试';", search_input)
print("✅ 元素可点击，已通过 JS 填入文字")

driver.quit()