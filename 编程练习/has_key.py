def has_key(datas, key):
    lists = list(datas.keys())
    for i in lists:
        if i==key:
            return True
    return False

data = {"name": "张三", "age": 20}

print(has_key(data, "name"))
print(has_key(data, "city"))
print(has_key(data, "age"))
