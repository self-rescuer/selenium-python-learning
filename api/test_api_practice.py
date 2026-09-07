import pytest
import requests


@pytest.fixture
def base_url():
    return "https://httpbin.org"


def test_get_request(base_url):
    """测试 GET 请求：验证状态码和响应头"""
    response = requests.get(f"{base_url}/get", params={"name": "张三"})

    # 断言状态码
    assert response.status_code == 200

    # 断言 Content-Type
    assert "application/json" in response.headers["Content-Type"]

    # 断言返回的 args 包含我们传的参数
    data = response.json()
    assert data["args"]["name"] == "张三"


def test_post_json(base_url):
    """测试 POST 请求：发送 JSON 数据并验证原样返回"""
    payload = {
        "user": "测试开发",
        "skills": ["Python", "Pytest", "Requests"]
    }

    response = requests.post(f"{base_url}/post", json=payload)

    # 断言状态码
    assert response.status_code == 200

    # 断言返回的 JSON 数据与我们发送的一致
    data = response.json()
    assert data["json"] == payload


def test_post_headers(base_url):
    """测试 POST 请求：自定义 Header 被服务器正确接收"""
    custom_headers = {
        "X-Test-Header": "hello-pytest",
        "User-Agent": "my-pytest-client"
    }

    response = requests.post(
        f"{base_url}/post",
        json={"key": "value"},
        headers=custom_headers
    )

    assert response.status_code == 200

    data = response.json()
    assert data["headers"]["X-Test-Header"] == "hello-pytest"
    assert data["headers"]["User-Agent"] == "my-pytest-client"