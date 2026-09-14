import sys
import os
import allure
import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.assert_utils import AssertUtils


@allure.feature("GitHub 用户接口")
class TestGitHubUsers:

    @allure.story("获取用户信息")
    @allure.title("获取 octocat 用户信息")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_get_user_info(self, client):
        with allure.step("发送 GET 请求"):
            response = client.get("/users/octocat")

        with allure.step("断言状态码为 200"):
            AssertUtils.assert_status_code(response, 200)

        with allure.step("断言字段和类型"):
            data = response.json()
            AssertUtils.assert_value_equal(data, "login", "octocat")
            AssertUtils.assert_type(data, "id", int)

    @allure.story("错误处理")
    @allure.title("请求不存在的用户返回 404")
    def test_get_nonexistent_user(self, client):
        with allure.step("发送 GET 请求"):
            response = client.get("/users/this-user-should-not-exist-123456789")

        with allure.step("断言状态码为 404"):
            AssertUtils.assert_status_code(response, 404)