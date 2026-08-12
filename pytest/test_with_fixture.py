# test_with_fixture.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_baidu_search(browser):  # 参数名与 fixture 名称一致
    driver = browser  # browser 就是 fixture 返回的 driver
    driver.get("https://www.baidu.com")

    wait = WebDriverWait(driver, 60)
    search_input = wait.until(EC.presence_of_element_located((By.ID, 'kw')))
    driver.execute_script("arguments[0].value = 'Pytest fixture';", search_input)

    search_btn = wait.until(EC.presence_of_element_located((By.ID, 'su')))
    driver.execute_script("arguments[0].click();", search_btn)

    wait.until(EC.presence_of_element_located((By.ID, 'content_left')))
    titles = driver.find_elements(By.CSS_SELECTOR, ".result h3")

    found = False
    for title in titles[:5]:
        if "Pytest" in title.text:
            found = True
            break

    assert found, "未找到包含'Pytest'的标题"