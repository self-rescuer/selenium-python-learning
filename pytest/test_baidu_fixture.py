from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from conftest import browser


def test_baidu_search(browser):
    driver = browser
    driver.get("https://www.baidu.com")

    wait = WebDriverWait(driver, 60)
    search_input = wait.until(EC.presence_of_element_located((By.ID, 'kw')))
    driver.execute_script("arguments[0].value = 'Pytest自动化测试';", search_input)

    search_btn = wait.until(EC.presence_of_element_located((By.ID, 'su')))
    driver.execute_script("arguments[0].click();", search_btn)

    wait.until(EC.presence_of_element_located((By.ID, 'content_left')))
    titles = driver.find_elements(By.CSS_SELECTOR, ".result h3")

    # 断言：至少有一条结果标题包含搜索词
    found = False
    for title in titles[:5]:
        if "Pytest" in title.text:
            found = True
            break

    assert found, "搜索结果中未找到包含'Pytest'的标题"

    time.sleep(2)