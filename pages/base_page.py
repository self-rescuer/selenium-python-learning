from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """页面对象基类，封装通用的元素操作"""

    def __init__(self, driver, timeout=30):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def find_element(self, locator):
        """等待元素可见后返回该元素"""
        return self.wait.until(EC.presence_of_element_located(locator))
    def find_elements(self, locator):
        """等待至少一个元素出现在 DOM 后返回元素列表"""
        self.wait.until(EC.presence_of_all_elements_located(locator))
        return self.driver.find_elements(*locator)

    def click(self, locator):
        """使用 execute_script 触发点击，绕过百度首页交互检查"""
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].click();", element)

    def input_text(self, locator, text):
        """使用 execute_script 设置输入框的值"""
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].value = arguments[1];", element, text)

    def get_text(self, locator):
        """获取单个元素的文本"""
        element = self.find_element(locator)
        return element.text

    def get_elements_text(self, locator):
        """获取多个元素的文本列表"""
        elements = self.find_elements(locator)
        return [el.text for el in elements]