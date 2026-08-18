def find_max(lis):
    for j in range(len(lis)):
        if j==0:
            i=lis[j]
        elif lis[j]>i:
            i=lis[j]
    return i
lis1=[0,7,9,4,5,8,3]
find_max(lis1)
'''
# 写一个函数 find_max(lst)，返回列表中的最大值。
# 
# 要求：
# 
# 不能使用内置函数 max()
# 
# 可以手写循环，逐个比较
# 
# 假设列表非空，且元素都是数字
'''