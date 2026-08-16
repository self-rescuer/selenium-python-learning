import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_pure():
    driver = webdriver.Chrome()
    try:
        driver.get("https://www.baidu.com")
        time.sleep(3)  # 强制等待页面加载
        search_input = driver.find_element(By.ID, 'kw')
        search_input.send_keys("Selenium")
        time.sleep(1)
        search_btn = driver.find_element(By.ID, 'su')
        search_btn.click()
        time.sleep(3)
        titles = driver.find_elements(By.CSS_SELECTOR, ".result h3")
        assert len(titles) > 0
    finally:
        driver.quit()