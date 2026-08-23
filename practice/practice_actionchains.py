from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import os
import time
import os

# 启动浏览器
options = Options()
options.add_argument("--remote-allow-origins=*")
driver = webdriver.Chrome(options=options)

try:

    # 获取当前脚本所在目录
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = "file://" + os.path.join(script_dir, "practice.html")
    driver.get(file_path)
    time.sleep(1)

    # 1. 鼠标悬停
    hover_box = driver.find_element(By.ID, "hover-box")
    ActionChains(driver).move_to_element(hover_box).perform()
    print("悬停完成")
    time.sleep(1)

    # 2. 拖拽
    source = driver.find_element(By.ID, "drag-source")
    target = driver.find_element(By.ID, "drop-target")
    ActionChains(driver).drag_and_drop(source, target).perform()
    print("拖拽完成")
    time.sleep(1)

finally:
    driver.quit()
