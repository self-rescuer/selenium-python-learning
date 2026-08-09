def count_vowels(text):
    num=0
    vowels='aeiouAEIOU'
    for i in text:
        if i in vowels:
            num+=1
    print(f'元音字母数量为:{num}')
    return num
text1='watermelon is delicious'
count_vowels(text1)

'''
写一个函数 count_vowels(text)，接收一个字符串，返回其中元音字母（a, e, i, o, u）的个数。
不区分大小写，A 和 a 都算。

示例：
count_vowels("Hello") → 2 (e, o)
count_vowels("Python") → 1 (o)
count_vowels("Selenium") → 4 (e, e, i, u)
'''