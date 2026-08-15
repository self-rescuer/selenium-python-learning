def merge_dicts(dict1,dict2):
    dict1.update(dict2)
    print(dict1)
dict01={'q':7,'w':7,'e':9}
dict02={'o':6,'w':8}
merge_dicts(dict01,dict02)

'''
# 写一个函数 merge_dicts(dict1, dict2)，接收两个字典，返回合并后的字典
# 如果两个字典有相同的键，dict2 的值覆盖 dict1 的值

# 示例：
# merge_dicts({'a': 1, 'b': 2}, {'b': 3, 'c': 4}) → {'a': 1, 'b': 3, 'c': 4}
# merge_dicts({'name': 'Tom', 'age': 20}, {'age': 21, 'city': 'Beijing'}) → {'name': 'Tom', 'age': 21, 'city': 'Beijing'}
# merge_dicts({'x': 1}, {'y': 2}) → {'x': 1, 'y': 2}
'''