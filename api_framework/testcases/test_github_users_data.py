import sys
import os
import json
import allure
import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.assert_utils import AssertUtils


current_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(current_dir, "..", "data", "users.json")

with open(data_path, encoding="utf-8") as f:
    users = json.load(f)["users"]

usernames = [user["username"] for user in users]


@allure.feature("GitHub 用户接口 - 数据驱动")
class TestGitHubUsersData:

    @allure.story("多用户测试")
    @pytest.mark.parametrize("username", usernames)
    def test_get_user_by_username(self, client, username):
        with allure.step(f"查询用户 {username}"):
            response = client.get(f"/users/{username}")

        with allure.step("断言状态码为 200"):
            AssertUtils.assert_status_code(response, 200)

        with allure.step(f"断言用户名为 {username}"):
            data = response.json()
            AssertUtils.assert_value_equal(data, "login", username)