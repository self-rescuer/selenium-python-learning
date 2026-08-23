"""
def count_substring(text, sub):
    count = 0
    for i in range(len(text)):
        if text[i] == sub[0]:
            new = text[i:i + len(sub)]
            if new == sub:
                count += 1
                i += len(sub)
            else:
                i += 1
        else:
            i += 1
    return count


print(count_substring('my love is for myself', 'my'))
"""


def count_substring(text, sub):
    count = 0
    i = 0
    if sub == '':
        return 0
    else:
        while i <len(text):
            if text[i] == sub[0]:
                new = text[i:i + len(sub)]
                if new == sub:
                    count += 1
                    i += len(sub)
                else:
                    i += 1
            else:
                i += 1
    return count


print(count_substring('my love is for myself', 'my'))
print(count_substring("aaa", "aa"))
