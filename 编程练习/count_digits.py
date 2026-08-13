def count_digits(text):
    print( sum(1 for ch in text if ch in '0123456789'))
test1='784lllxxx'
count_digits(test1)