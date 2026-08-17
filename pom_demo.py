from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.baidu_page import BaiduHomePage, BaiduResultPage


# 启动浏览器
options = Options()
options.add_argument("--remote-allow-origins=*")
driver = webdriver.Chrome(options=options)

try:
    # 使用 Page 对象操作
    home = BaiduHomePage(driver)
    home.open()
    home.search("测试开发")

    result = BaiduResultPage(driver)
    titles = result.get_titles()

    # 打印前 5 条标题
    print("搜索结果前 5 条：")
    for i, title in enumerate(titles[:5], 1):
        print(f"{i}. {title}")

finally:
    # 无论成功失败都关闭浏览器
    driver.quit()