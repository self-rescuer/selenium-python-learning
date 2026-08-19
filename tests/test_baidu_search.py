import pytest
from pages.baidu_page import BaiduHomePage, BaiduResultPage


def test_baidu_search(browser):
    """测试百度搜索：输入关键词，验证有搜索结果返回"""
    keyword = "测试开发"

    # 使用 Page 对象操作
    home = BaiduHomePage(browser)
    home.open()
    home.search(keyword)

    result = BaiduResultPage(browser)
    titles = result.get_titles()

    # 断言：至少返回一条结果
    assert len(titles) > 0, "搜索未返回任何结果"

    # 可选：打印第一条标题，方便查看
    print(f"第一条结果标题: {titles[0]}")