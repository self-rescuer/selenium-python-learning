import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json
import os

@pytest.fixture(scope="function")
def browser():
    """启动浏览器，测试结束后自动关闭"""
    options = Options()
    options.add_argument("--remote-allow-origins=*")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

@pytest.fixture
def search_data():
    """从 JSON 文件中读取测试数据"""
    # 注意：conftest.py 在根目录，JSON 文件在 pytest/ 子目录下
    current_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(current_dir, "pytest", "test_data.json")
    with open(json_path, 'r', encoding='utf-8') as f:
        return json.load(f)