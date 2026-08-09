try:
    with open('../test.txt', 'r', encoding='utf-8')as f:
        test=f.read()
        test1=test.split()
        num=len(test1)
        print(test1)
        print(f'文件里单词的个数是:{num}')
except FileNotFoundError:
    print('文件未找到，请检查路径')

'''
写一个函数，读取一个文本文件，统计文件里一共有多少个单词（按空格分割）。
要求：
1.手动创建一个 test.txt 文件，里面随便写 3-5 个英文句子。
2.用 with open 读取该文件。
3.用 split() 按空格分割，统计单词数量。
4.用 print 输出结果。
5.加上 try/except，如果文件不存在，输出友好的提示信息 "文件未找到，请检查路径"。
'''