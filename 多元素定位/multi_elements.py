from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")

# 设置超时为60秒，足够应付人机验证
wait = WebDriverWait(driver, 60)

# 1. 输入搜索词
search_input = wait.until(EC.presence_of_element_located((By.ID, "kw")))
driver.execute_script("arguments[0].value = 'Selenium自动化测试';", search_input)
print("输入框已填值")

# 2. 点击搜索按钮
search_btn = wait.until(EC.presence_of_element_located((By.ID, "su")))
driver.execute_script("arguments[0].click();", search_btn)
print("搜索按钮已点击，如有验证码请手动通过...")

# 3. 等待页面标题包含关键词（或者等待URL变化）
try:
    wait.until(EC.title_contains("Selenium自动化测试"))
    print("页面已跳转（标题包含关键词）")
except:
    # 如果标题条件超时，尝试等待URL包含参数
    wait.until(EC.url_contains("wd="))
    print("页面已跳转（URL包含搜索参数）")

# 4. 等待结果容器加载
wait.until(EC.presence_of_element_located((By.ID, "content_left")))
print("结果已加载")

# 5. 获取所有结果标题
titles = driver.find_elements(By.CSS_SELECTOR, ".result h3")
print(f"找到 {len(titles)} 条结果")

# 6. 遍历前10条
for i, title in enumerate(titles[:10]):
    try:
        link = title.find_element(By.XPATH, "./a").get_attribute("href")
        print(f"{i+1}. 标题：{title.text}")
        print(f"   链接：{link}")
        print()
    except:
        print(f"{i+1}. 标题：{title.text}（无法获取链接）")

time.sleep(3)
driver.quit()