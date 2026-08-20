import allure
from pages.baidu_page import BaiduHomePage, BaiduResultPage


@allure.feature("百度搜索")
@allure.story("搜索功能")
@allure.severity(allure.severity_level.NORMAL)
def test_baidu_search(browser):
    keyword = "测试开发"

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