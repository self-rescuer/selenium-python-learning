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