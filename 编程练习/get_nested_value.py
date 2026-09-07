def get_nested_value(data,key1,key2):
    return data[key1][key2]

data = {
        "user": {
            "name": "张三",
            "age": 20
        },
        "status": "active"
    }
print(get_nested_value(data, "user", "name"))
print(get_nested_value(data, "user", "age"))
