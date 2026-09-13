"""
def flatten_dict(data):
    result={}
    for i in data:
        if type(data[i]) is dict:
            for j in data[i]:
                if type(data[i][j]) is dict:
                    for k in data[i][j]:
                        result[f'{i}.{j}.{k}'] = data[i][j][k]
                else:
                    result[f'{i}.{j}'] = data[i][j]
        else:
            result[f'{i}'] = data[i]
    return result


datas = {
    "user": {
        "name": "张三",
        "address": {
            "city": "武汉",
            "district": "洪山区"
        }
    },
    "active": True
}

print( flatten_dict(datas))
"""
def flatten_dict(data, parent_key=''):
    result = {}
    for key, value in data.items():
        new_key = f"{parent_key}.{key}" if parent_key else key

        if isinstance(value, dict):
            # 递归处理嵌套字典
            result.update(flatten_dict(value, new_key))
        else:
            result[new_key] = value

    return result

data = {
    "user": {
        "name": "张三",
        "address": {
            "city": "武汉",
            "district": "洪山区"
        }
    },
    "active": True
}

print(flatten_dict(data))
# 输出 {
#     'user.name': '张三',
#     'user.address.city': '武汉',
#     'user.address.district': '洪山区',
#     'active': True
# }
