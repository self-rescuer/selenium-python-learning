def count_words_starting_with(text,letter):
    cleaned =text.lower().split()
    res=(i for i in cleaned if i[0]==letter.lower())
    ret=list(res)
    print(f'以{letter}开头的字母数量为{len(ret)}')
count_words_starting_with('world needs you,I need you','n')

'''
 写一个函数 count_words_starting_with(text, letter)
 统计 text 中，以指定字母开头的单词有多少个
 不区分大小写
 示例：
 count_words_starting_with("Python is great, Python is powerful", "p") → 2
 count_words_starting_with("Hello world, hello everyone", "h") → 2
count_words_starting_with("apple banana avocado", "a") → 2
'''


'''
以下为AI优化版本:
def count_words_starting_with(text, letter):
    cleaned = text.lower().split()
    return sum(1 for word in cleaned if word.startswith(letter.lower()))

print(count_words_starting_with('world needs you,I need you', 'n'))  # 输出 2
'''