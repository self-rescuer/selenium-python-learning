def merge_lists(list1,list2):
    for i in list2:
        if i not in list1:
            list1.append(i)
    print(list1)
list01=[0,4,8,7,9]
list02=[5,7,4,6,5]
merge_lists(list01,list02)

'''
# 写一个函数 merge_lists(list1, list2)，接收两个列表，返回合并后的列表
# 要求：返回的列表中不包含重复元素，且保持原顺序（先 list1 的顺序，再 list2 中新增元素的顺序）

# 示例：
# merge_lists([1, 2, 3], [2, 3, 4]) → [1, 2, 3, 4]
# merge_lists(['a', 'b'], ['b', 'c', 'd']) → ['a', 'b', 'c', 'd']
# merge_lists([1, 2], [3, 4]) → [1, 2, 3, 4]
'''