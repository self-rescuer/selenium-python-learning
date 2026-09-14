import time
import requests
from requests.exceptions import Timeout, ConnectionError, RequestException
from core.config_manager import ConfigManager
from core.logger import get_logger
import allure


class RequestClient:
    """接口请求客户端，统一封装 GET/POST/PUT/DELETE"""

    def __init__(self, config_file="config.json"):
        self.config = ConfigManager(config_file)
        self.base_url = self.config.base_url
        self.timeout = self.config.timeout
        self.headers = self.config.headers
        self.logger = get_logger(self.__class__.__name__)

    def _request(self, method, path, retries=3, **kwargs):
        url = self.base_url + path
        headers = {**self.headers, **kwargs.pop("headers", {})}
        kwargs.setdefault("timeout", self.timeout)

        self.logger.info(f"请求 {method} {url}")

        for attempt in range(1, retries + 1):
            try:
                response = requests.request(method, url, headers=headers, **kwargs)
                self.logger.info(f"响应状态码: {response.status_code}")
                self.logger.info(f"响应内容: {response.text[:200]}")

                allure.attach(
                    f"请求: {method} {url}\n"
                    f"请求参数: {kwargs.get('params', {})}\n"
                    f"请求体: {kwargs.get('json', {})}\n"
                    f"响应状态码: {response.status_code}\n"
                    f"响应内容: {response.text[:2000]}",
                    name=f"{method} {path}",
                    attachment_type=allure.attachment_type.TEXT
                )

                return response

            except Timeout:
                self.logger.warning(f"第 {attempt} 次请求超时")
            except ConnectionError:
                self.logger.warning(f"第 {attempt} 次请求连接失败")
            except RequestException as e:
                self.logger.error(f"请求异常: {e}")
                raise

            if attempt < retries:
                time.sleep(1)

        raise Timeout(f"请求 {url} 重试 {retries} 次后仍失败")

    def get(self, path, **kwargs):
        return self._request("GET", path, **kwargs)

    def post(self, path, **kwargs):
        return self._request("POST", path, **kwargs)

    def put(self, path, **kwargs):
        return self._request("PUT", path, **kwargs)

    def delete(self, path, **kwargs):
        return self._request("DELETE", path, **kwargs)