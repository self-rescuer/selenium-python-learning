from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class BaiduHomePage(BasePage):
    SEARCH_INPUT = (By.ID, "kw")
    SEARCH_BUTTON = (By.ID, "su")
    URL = "https://www.baidu.com"

    def open(self):
        self.driver.get(self.URL)

    def search(self, keyword):
        self.input_text(self.SEARCH_INPUT, keyword)
        self.click(self.SEARCH_BUTTON)


class BaiduResultPage(BasePage):
    RESULT_TITLES = (By.CSS_SELECTOR, "h3.t a")

    def get_titles(self):
        return self.get_elements_text(self.RESULT_TITLES)