import  pytest
from selenium import webdriver
@pytest.fixture
def browser():
    driver=webdriver.Chrome()
    yield driver
    driver.quit()


import os
import json
import pytest
@pytest.fixture
def search_data():
    """从 JSON 文件中读取测试数据"""
    # 获取当前文件所在目录，构建 JSON 文件的完整路径
    current_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(current_dir, "pytest", "test_data.json")

    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data