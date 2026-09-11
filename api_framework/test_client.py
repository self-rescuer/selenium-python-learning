import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from core.request_client import RequestClient

client = RequestClient()

# 测试 GET
response = client.get("/users/octocat")
print("状态码:", response.status_code)
print("用户名:", response.json()["login"])

# 临时把 base_url 换成 httpbin 测试 POST
client.base_url = "https://httpbin.org"
response = client.post("/post", json={"name": "张三"})
print("POST 状态码:", response.status_code)
print("POST 返回:", response.json()["json"])