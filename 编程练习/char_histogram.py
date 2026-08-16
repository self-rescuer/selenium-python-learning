def char_histogram(text):
    res={}
    for i in text:
        if not i.isalpha():
            continue
        if i in res:
            res[i]+=1
        else:
            res[i]=1
    print(res)
text1='ahasaq'
char_histogram(text1)

'''
# 写一个函数 char_histogram(text)，接收一个字符串，返回每个字符出现次数的字典
# 要求：忽略空格，只统计字母
# 示例：
# char_histogram("banana") → {'b': 1, 'a': 3, 'n': 2}
# char_histogram("hello world") → {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}
'''
