def remove_chars(text,chars):
    res=''.join(i for i in text if i not in chars)
    print(res)
    return res
text1='apple'
chars1='ae'
remove_chars(text1,chars1)