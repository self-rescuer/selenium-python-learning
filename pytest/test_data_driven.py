import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_baidu_search(browser, search_data):
    """使用 JSON 数据驱动搜索测试"""
    for item in search_data:
        driver = browser
        driver.get("https://www.baidu.com")
        wait = WebDriverWait(driver, 60)
        search_input = wait.until(EC.presence_of_element_located((By.ID, 'kw')))
        driver.execute_script("arguments[0].value = arguments[1];", search_input, item['word'])
        search_btn = wait.until(EC.presence_of_element_located((By.ID, 'su')))
        driver.execute_script("arguments[0].click();", search_btn)
        wait.until(EC.presence_of_element_located((By.ID, 'content_left')))
        titles = driver.find_elements(By.CSS_SELECTOR, ".result h3")
        found = any(item['expected'] in title.text for title in titles[:5])
        assert found, f"搜索 '{item['word']}' 失败，前5条结果中未找到 '{item['expected']}'"
        print(f"✅ 搜索 '{item['word']}' 通过")