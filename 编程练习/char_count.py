def char_count(text):
    res={}
    for i in text:
        if i==' ':
            continue
        elif i in res:
            res[i]+=1
        else:
            res[i]=1
    print(res)
ts1='abccbasd'
char_count(ts1)


'''
# 写一个函数 char_count(text)，接收一个字符串，返回一个字典
# 字典的键是字符串中出现的字符，值是该字符出现的次数
# 忽略空格

# 示例：
# char_count("hello") → {'h': 1, 'e': 1, 'l': 2, 'o': 1}
# char_count("abracadabra") → {'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1}
# char_count("hello world") → {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}
'''

