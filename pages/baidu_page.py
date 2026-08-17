from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaiduHomePage:
    # 定位器集中管理
    SEARCH_INPUT = (By.ID, "kw")
    SEARCH_BUTTON = (By.ID, "su")
    URL = "https://www.baidu.com"

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        # 打开百度首页
        self.driver.get(self.URL)

    def _set_input_value(self, element, value):
        # 用 execute_script 设置输入框的值，绕过不可交互检查
        self.driver.execute_script("arguments[0].value = arguments[1];", element, value)

    def _click(self, element):
        # 用 execute_script 触发点击
        self.driver.execute_script("arguments[0].click();", element)

    def search(self, keyword):
        # 找到搜索框和搜索按钮
        input_box = self.driver.find_element(*self.SEARCH_INPUT)
        search_btn = self.driver.find_element(*self.SEARCH_BUTTON)

        # 输入关键词并点击
        self._set_input_value(input_box, keyword)
        self._click(search_btn)


class BaiduResultPage:
    RESULT_TITLES = (By.CSS_SELECTOR, "h3.t a")

    def __init__(self, driver):
        self.driver = driver

    def get_titles(self):
        # 等待至少一个结果标题出现，最多等10秒
        WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located(self.RESULT_TITLES)
        )

        elements = self.driver.find_elements(*self.RESULT_TITLES)
        return [el.text for el in elements]