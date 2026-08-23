from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import os
import time
import os

# 启动浏览器
options = Options()
options.add_argument("--remote-allow-origins=*")
driver = webdriver.Chrome(options=options)

try:
    # 打开本地 HTML 文件

    # 获取当前脚本所在目录
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = "file://" + os.path.join(script_dir, "practice.html")
    driver.get(file_path)

    # 等待页面加载
    time.sleep(1)

    # 定位下拉框
    select_element = driver.find_element("id", "fruit")
    select = Select(select_element)

    # 1. 通过 visible text 选择
    select.select_by_visible_text("苹果")
    print("当前选择:", select.first_selected_option.text)

    time.sleep(1)

    # 2. 通过 value 选择
    select.select_by_value("banana")
    print("当前选择:", select.first_selected_option.text)

    time.sleep(1)

    # 3. 通过 index 选择（从0开始）
    select.select_by_index(3)  # orange
    print("当前选择:", select.first_selected_option.text)

    time.sleep(1)

finally:
    driver.quit()
