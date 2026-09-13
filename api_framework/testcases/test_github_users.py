import sys
import os
import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.assert_utils import AssertUtils


class TestGitHubUsers:
    """测试 GitHub 用户接口"""

    def test_get_user_info(self, client):
        response = client.get("/users/octocat")

        AssertUtils.assert_status_code(response, 200)

        data = response.json()
        AssertUtils.assert_key_exists(data, "login")
        AssertUtils.assert_key_exists(data, "id")
        AssertUtils.assert_value_equal(data, "login", "octocat")
        AssertUtils.assert_type(data, "id", int)
        AssertUtils.assert_type(data, "public_repos", int)

    def test_get_nonexistent_user(self, client):
        response = client.get("/users/this-user-should-not-exist-123456789")

        AssertUtils.assert_status_code(response, 404)

        data = response.json()
        AssertUtils.assert_value_equal(data, "message", "Not Found")