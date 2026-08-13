from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

import pytest

@pytest.mark.parametrize("word, expected", [
    ("Selenium", "Selenium"),
    ("Pytest", "Pytest"),
    ("自动化测试", "自动化")
])
def test_baidu_search(browser, word, expected):
    driver = browser
    driver.get("https://www.baidu.com")
    wait = WebDriverWait(driver, 60)
    search_input = wait.until(EC.presence_of_element_located((By.ID, 'kw')))
    driver.execute_script("arguments[0].value = arguments[1];", search_input, word)
    search_btn = wait.until(EC.presence_of_element_located((By.ID, 'su')))
    driver.execute_script("arguments[0].click();", search_btn)
    wait.until(EC.presence_of_element_located((By.ID, 'content_left')))
    titles = driver.find_elements(By.CSS_SELECTOR, ".result h3")
    found = any(expected in title.text for title in titles[:5])
    assert found, f"在搜索结果的前5条中未找到 '{expected}'"