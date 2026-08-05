from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

class MyWait:
    """自定义等待类，每次轮询都在控制台打印一条日志"""
    def __init__(self, driver, timeout):
        self.driver = driver
        self.timeout = timeout
        self.interval = 0.5

    def until(self, condition):
        start_time = time.time()
        loop_count = 0
        while True:
            loop_count += 1
            elapsed = time.time() - start_time
            print(f"第 {loop_count} 次轮询，已等待 {elapsed:.2f} 秒")
            try:
                result = condition(self.driver)
                if result:
                    print("找到元素！跳出循环")
                    return result
            except NoSuchElementException:
                # 找不到元素，不报错，继续下一次轮询
                pass
            if elapsed >= self.timeout:
                raise Exception(f"超时！已等待 {elapsed:.2f} 秒，共轮询 {loop_count} 次")
            time.sleep(self.interval)

if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.get("https://www.baidu.com")

    custom_wait = MyWait(driver, 10)
    print("开始查找不存在的元素，观察下方轮询日志...")
    try:
        element = custom_wait.until(lambda d: d.find_element(By.ID, "this_id_does_not_exist"))
    except Exception as e:
        print(f"报错: {e}")
    finally:
        driver.quit()