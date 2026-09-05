import requests
response = requests.get("https://api.github.com/users/octocat")
print('状态码:',response.status_code)
data=response.json()
print('用户名:',data['login'])
print('用户id:',data['id'])
print('名字:',data['name'])
print('Content_Type:',response.headers['Content-Type'])