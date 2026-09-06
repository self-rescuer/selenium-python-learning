def build_dict(keys, values):
    dic = {}
    for n in range(len(keys)):
        dic[keys[n]] = values[n]
    return dic
print(build_dict(["name", "age"], ["张三", 20]))

print(build_dict(["a", "b", "c"], [1, 2, 3]))