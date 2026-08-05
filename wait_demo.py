from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.baidu.com")

    # 超时设到 60 秒，给你留足手动验证的时间
    wait = WebDriverWait(driver, 60)

    print("等待输入框出现（如有验证码请手动通过）...")
    search_input = wait.until(EC.presence_of_element_located((By.ID, "kw")))
    driver.execute_script("arguments[0].value = 'Selenium等待';", search_input)
    print("输入框已填值")

    print("等待搜索按钮...")
    search_button = wait.until(EC.presence_of_element_located((By.ID, "su")))
    driver.execute_script("arguments[0].click();", search_button)
    print("搜索按钮已点击")

    # 等待结果容器出现
    wait.until(EC.presence_of_element_located((By.ID, "content_left")))
    print("搜索结果已加载")

    time.sleep(5)
    print("脚本执行完毕！浏览器将在3秒后关闭")
    time.sleep(3)
    driver.quit()