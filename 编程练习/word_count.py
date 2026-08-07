try:
    with open('../test.txt', 'r', encoding='utf-8')as f:
        test=f.read()
        test1=test.split()
        num=len(test1)
        print(test1)
        print(f'文件里单词的个数是:{num}')
except FileNotFoundError:
    print('文件未找到，请检查路径')
