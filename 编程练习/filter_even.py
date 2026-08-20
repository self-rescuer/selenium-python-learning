def filter_even(lst):
    res=[]
    for i in lst:
        if i%2==0:
            res.append(i)
    return res
print(filter_even([1,3,5,8,9,4,7]))


'''
题目：过滤偶数

写一个函数 filter_even(lst)，返回一个新列表，其中只包含原列表中的偶数。

要求：

不能使用内置函数 filter()

手写循环，逐个判断

保持原列表中元素的顺序

返回新列表，不修改原列表
'''