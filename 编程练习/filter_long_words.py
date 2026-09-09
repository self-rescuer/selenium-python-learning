def filter_long_words(words,n):
    filtered_words = []
    for word in words:
        if len(word) >= n:
            filtered_words.append(word)
    return filtered_words
print(filter_long_words(["hello", "world", "python", "ai"], 5))

print(filter_long_words(["a", "bb", "ccc"], 2))
