def fibonacci(n):
    if not isinstance(n, int):
        return '请输入整数'
    elif n < 0:
        return '输入的整数应大于等于零'
    elif n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(6))
print(fibonacci(10))
