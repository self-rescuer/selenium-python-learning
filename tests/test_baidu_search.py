import os
import json
import allure
import pytest
from pages.baidu_page import BaiduHomePage, BaiduResultPage


# 从 JSON 文件读取测试数据
current_dir = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(current_dir, "..", "data", "test_data.json")
with open(json_path, encoding='utf-8') as f:
    keywords = [item["keyword"] for item in json.load(f)]


@allure.feature("百度搜索")
@allure.story("搜索功能")
@pytest.mark.parametrize("keyword", keywords)
def test_baidu_search(browser, keyword):
    with allure.step("打开百度首页"):
        home = BaiduHomePage(browser)
        home.open()

    with allure.step(f"搜索关键词：{keyword}"):
        home.search(keyword)

    with allure.step("获取搜索结果"):
        result = BaiduResultPage(browser)
        titles = result.get_titles()

    with allure.step("断言有搜索结果"):
        assert len(titles) > 0
        allure.attach(str(titles[:5]), "前5条标题", allure.attachment_type.TEXT)