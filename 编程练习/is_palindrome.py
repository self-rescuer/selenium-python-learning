def is_palindrome(text):
    cleaned = ''.join(ch for ch in text.lower() if ch.isalpha())
    return cleaned == cleaned[::-1]
text1='Qtx i78 xtq'
print(is_palindrome(text1))


''' 
写一个函数 is_palindrome(text)，接收一个字符串，判断它是否为回文
回文定义：正读和反读相同，忽略大小写，不考虑空格和标点符号
只考虑字母字符（a-z 和 A-Z）

# 示例：
# is_palindrome("abcba") → True
# is_palindrome("hello") → False
# is_palindrome("A man a plan a canal Panama") → True  （忽略空格和大小写）
# is_palindrome("race a car") → False
'''