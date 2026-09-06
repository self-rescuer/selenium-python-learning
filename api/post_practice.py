import requests

# 1. 发送 JSON 数据的 POST 请求
url = "https://httpbin.org/post"

data = {
    "name": "张三",
    "age": 20,
    "skills": ["Python", "Selenium", "Requests"]
}

headers = {
    "User-Agent": "my-test-client",
    "X-Custom-Header": "hello"
}

response = requests.post(url, json=data, headers=headers)

# 2. 查看状态码
print("状态码：", response.status_code)

# 3. 查看服务器返回的 JSON
result = response.json()

# httpbin 会把我们发送的数据原样返回
print("我们发送的 JSON：", result["json"])
print("我们发送的 Header：", result["headers"]["X-Custom-Header"])
print("我们发送的 User-Agent：", result["headers"]["User-Agent"])

# 4. 查看服务器返回的 Content-Type
print("响应 Content-Type：", response.headers["Content-Type"])