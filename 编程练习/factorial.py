def factorial(n):
    result=n
    if type(n) is not int:
        return '请输入整数'
    elif n < 0:
        return '请输入非负整数'
    elif n == 0:
        return 1
    else:
        while n>1:
            n-=1
            result=result*n
        return result
print(factorial(0))
print(factorial(4))


