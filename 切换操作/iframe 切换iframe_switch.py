from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.w3schools.com/html/html_iframe.asp")

# 1. 打印主页面标题
print(f"主页面标题: {driver.title}")

# 2. 查看页面中有几个 iframe
iframes = driver.find_elements(By.TAG_NAME, "iframe")
print(f"页面中有 {len(iframes)} 个 iframe")

# 3. 切入第一个 iframe（索引 0）
driver.switch_to.frame(0)
print("已切入 iframe")

# 4. 在 iframe 内部定位元素并打印文本（例如查找 h1 标签）
# 提示：iframe 内部可能包含一个完整的页面，尝试找 h1 或 p 标签
inner_element = driver.find_element(By.TAG_NAME, "h1")
print(f"iframe 内部的 h1 文本: {inner_element.text}")

# 5. 切回主页面
driver.switch_to.default_content()
print("已切回主页面")

# 6. 再次定位主页面元素，确认已切回
main_element = driver.find_element(By.TAG_NAME, "h1")
print(f"主页面的 h1 文本: {main_element.text}")

time.sleep(2)
driver.quit()