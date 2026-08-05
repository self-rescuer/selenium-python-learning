from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.get("https://www.baidu.com")

    # 设置超时10秒
    wait = WebDriverWait(driver, 10)

    print("开始等待一个【不存在的元素】，接下来你会看到轮询过程...")
    # 故意找一个页面上绝对没有的 id，强迫它反复检查
    element = wait.until(EC.presence_of_element_located((By.ID, "this_id_does_not_exist")))

    print("这行不会被执行，因为上面必定超时")
    driver.quit()