import requests
from core.config_manager import ConfigManager
from core.logger import get_logger


class RequestClient:
    """接口请求客户端，统一封装 GET/POST/PUT/DELETE"""

    def __init__(self, config_file="config.json"):
        self.config = ConfigManager(config_file)
        self.base_url = self.config.base_url
        self.timeout = self.config.timeout
        self.headers = self.config.headers
        self.logger = get_logger(self.__class__.__name__)

    def _request(self, method, path, **kwargs):
        """所有请求的公共处理逻辑"""
        url = self.base_url + path

        # 合并公共 headers 和本次请求的 headers
        headers = {**self.headers, **kwargs.pop("headers", {})}

        # 如果没传 timeout，用配置里的
        kwargs.setdefault("timeout", self.timeout)

        self.logger.info(f"请求 {method} {url}")
        if "params" in kwargs:
            self.logger.info(f"请求参数: {kwargs['params']}")
        if "json" in kwargs:
            self.logger.info(f"请求体: {kwargs['json']}")

        response = requests.request(method, url, headers=headers, **kwargs)

        self.logger.info(f"响应状态码: {response.status_code}")
        self.logger.info(f"响应内容: {response.text[:200]}")

        return response

    def get(self, path, **kwargs):
        return self._request("GET", path, **kwargs)

    def post(self, path, **kwargs):
        return self._request("POST", path, **kwargs)

    def put(self, path, **kwargs):
        return self._request("PUT", path, **kwargs)

    def delete(self, path, **kwargs):
        return self._request("DELETE", path, **kwargs)