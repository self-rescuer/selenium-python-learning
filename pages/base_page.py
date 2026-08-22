from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import get_logger


class BasePage:
    """页面对象基类，封装通用的元素操作"""

    def __init__(self, driver, timeout=30):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
        self.logger = get_logger(self.__class__.__name__)

    def find_element(self, locator):
        self.logger.info(f"查找元素: {locator}")
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_elements(self, locator):
        self.logger.info(f"查找元素列表: {locator}")
        self.wait.until(EC.presence_of_all_elements_located(locator))
        return self.driver.find_elements(*locator)

    def click(self, locator):
        self.logger.info(f"点击元素: {locator}")
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].click();", element)

    def input_text(self, locator, text):
        self.logger.info(f"输入文本到 {locator}: {text}")
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].value = arguments[1];", element, text)

    def get_text(self, locator):
        self.logger.info(f"获取元素文本: {locator}")
        element = self.find_element(locator)
        return element.text

    def get_elements_text(self, locator):
        self.logger.info(f"获取元素列表文本: {locator}")
        elements = self.find_elements(locator)
        return [el.text for el in elements]