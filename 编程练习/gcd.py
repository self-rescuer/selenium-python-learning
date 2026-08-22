def gcd(a,b):
    if a<=b:
        for i in range(1,a+1):
            if a%i==0 and b%i==0:
                result=i
        return result
    else:
        return gcd(b,a)
print(gcd(34,8))

'''
题目：最大公约数

写一个函数 gcd(a, b)，返回两个正整数 a 和 b 的最大公约数。

要求：

不能使用 math.gcd() 或任何内置的公约数函数

手写循环实现（可以用辗转相除法，也可以枚举所有可能约数）

假设输入都是正整数

返回整数结果
'''