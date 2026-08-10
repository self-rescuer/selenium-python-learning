from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


'启动百度'
driver=webdriver.Chrome()
driver.get("https://www.baidu.com")

'等待输入框可交互并输入搜索词'
wait = WebDriverWait(driver, 60)
search_input=wait.until(EC.presence_of_element_located((By.ID,'kw')))
driver.execute_script("arguments[0].value = '自动化测试流程';", search_input)

'点击搜索按钮'
search_btn = wait.until(EC.presence_of_element_located((By.ID, 'su')))
driver.execute_script("arguments[0].click();", search_btn)

'等待结果并获取前五条结果，打印标题与链接'
wait.until(EC.presence_of_element_located((By.ID, 'content_left')))
titles = driver.find_elements(By.CSS_SELECTOR, ".result h3")
for i, title in enumerate(titles[:5]):
    link = title.find_element(By.XPATH, "./a").get_attribute("href")
    print(f'{i+1}. {title.text}')
    print(f'  链接：{link}')

'关闭浏览器'
time.sleep(3)
driver.quit()

