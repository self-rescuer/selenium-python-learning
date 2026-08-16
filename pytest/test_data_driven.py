import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import allure
import json
import os

@allure.feature("百度搜索")
@allure.story("数据驱动搜索")
def test_baidu_search():
    """使用 execute_script 操作百度搜索，数据驱动，并生成 Allure 报告"""
    driver = webdriver.Chrome()
    try:
        # 读取测试数据
        json_path = os.path.join(os.path.dirname(__file__), "test_data.json")
        with open(json_path, 'r', encoding='utf-8') as f:
            test_data = json.load(f)

        for item in test_data:
            with allure.step(f"搜索关键词: {item['word']}"):
                driver.get("https://www.baidu.com")
                time.sleep(2)  # 等待页面初始加载

                # 用 JavaScript 赋值（绕过交互检查）
                driver.execute_script(
                    "document.getElementById('kw').value = arguments[0];",
                    item['word']
                )
                time.sleep(0.5)

                # 用 JavaScript 点击搜索按钮
                driver.execute_script("document.getElementById('su').click();")
                print(f"已点击搜索按钮，等待结果...")

                # 等待搜索结果容器出现（最多 60 秒），如果出现人机验证，用户需手动通过
                for i in range(60):
                    try:
                        driver.find_element(By.ID, "content_left")
                        print("  搜索结果已加载")
                        break
                    except:
                        # 如果页面不是结果页，可能还在加载或验证中
                        print(f"  等待结果页... 第 {i+1} 秒")
                        time.sleep(1)
                else:
                    raise Exception("等待搜索结果超时（可能未通过人机验证或网络问题）")

                # 获取所有搜索结果标题（使用通用 h3 标签）
                titles = driver.find_elements(By.CSS_SELECTOR, "h3")
                print(f"关键词 '{item['word']}' 找到 {len(titles)} 条结果")

                # 断言至少有结果（确保搜索成功）
                assert len(titles) > 0, f"搜索 '{item['word']}' 未返回任何结果"

                # 可选：检查预期关键词是否在任意标题中
                found = any(item['expected'] in title.text for title in titles[:10])
                assert found, f"前10条结果中未找到预期词 '{item['expected']}'"

                # 截图附件
                allure.attach(
                    driver.get_screenshot_as_png(),
                    name=f"{item['word']}_搜索结果",
                    attachment_type=allure.attachment_type.PNG
                )
    finally:
        driver.quit()