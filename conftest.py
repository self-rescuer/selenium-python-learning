import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json
import os
import allure


@pytest.fixture(scope="function")
def browser():
    options = Options()
    options.add_argument("--remote-allow-origins=*")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


@pytest.fixture
def search_data():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(current_dir, "data", "test_data.json")
    with open(json_path, 'r', encoding='utf-8') as f:
        return json.load(f)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call":
        driver = item.funcargs.get("browser")
        if driver:
            screenshot = driver.get_screenshot_as_png()
            allure.attach(
                screenshot,
                name="screenshot",
                attachment_type=allure.attachment_type.PNG
            )