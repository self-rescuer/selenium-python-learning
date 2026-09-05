def word_count(text):
    text = text.lower()
    words=text.split(' ')
    result={}
    for word in words:
        if word in result:
            result[word]+=1
        else:
            result[word]=1
    return result
print(word_count("hello world hello"))
# 输出 {'hello': 2, 'world': 1}

print(word_count("Python is great and python is fun"))
# 输出 {'python': 2, 'is': 2, 'great': 1, 'and': 1, 'fun': 1}

