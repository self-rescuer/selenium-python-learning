from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
wait = WebDriverWait(driver, 60)

# 等待输入框并输入 selenium
search_input = wait.until(EC.presence_of_element_located((By.ID, 'kw')))
driver.execute_script("arguments[0].value = 'selenium';", search_input)
print('第一次输入完成')
time.sleep(1)

# 用 JavaScript 清空输入框
driver.execute_script("arguments[0].value = '';", search_input)
print('已清空')

# 用 JavaScript 输入 "自动化测试"
driver.execute_script("arguments[0].value = '自动化测试';", search_input)
print('第二次输入完成')

# 点击搜索按钮（也可以用 JS 点击）
search_btn = wait.until(EC.presence_of_element_located((By.ID, 'su')))
driver.execute_script("arguments[0].click();", search_btn)
print('已点击搜索')

# 等待结果并提取
wait.until(EC.presence_of_element_located((By.ID, 'content_left')))
titles = driver.find_elements(By.CSS_SELECTOR, ".result h3")
for i, title in enumerate(titles[:5]):
    link = title.find_element(By.XPATH, "./a").get_attribute("href")
    print(f'{i+1}. {title.text}')
    print(f'  链接：{link}')

time.sleep(3)
driver.quit()