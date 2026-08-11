def find_duplicates(text):
    seen = []
    duplicates = []
    for char in text:
        if char in seen:
            if char not in duplicates:
                duplicates.append(char)
        else:
            seen.append(char)
    print(duplicates)
text1='84fse4fa8354fe'
find_duplicates(text1)

'''
# 写一个函数 find_duplicates(lst)，接收一个列表，返回列表中所有重复出现的元素
# 每个重复元素只返回一次，顺序不限

# 示例：
# find_duplicates([1, 2, 3, 2, 1, 4]) → [1, 2]
# find_duplicates(['a', 'b', 'c', 'a', 'd']) → ['a']
# find_duplicates([1, 2, 3, 4]) → []
'''

'''
以下是AI优化版
def find_duplicates(lst):
    seen = set()
    duplicates = set()
    for item in lst:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    return list(duplicates)
'''
