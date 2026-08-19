def is_prime(n):
    if type(n) is not int:
        return False
    elif n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True



print(is_prime(17))
print(is_prime(15))



'''
写一个函数 is_prime(n)，判断一个整数是否为质数。

要求：

不能使用任何内置的数学判断函数

手写循环判断

负数、0、1 都不是质数

返回 True 或 False
'''