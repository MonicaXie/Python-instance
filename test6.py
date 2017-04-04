# 任务：输出前10个斐波那契数列。

def fib(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    fibs = [1, 1]
    for i in range(2, n):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs
print(fib(10))

# 输出结果

[1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

# 任务：输出第10个斐波那契数列。

# 方法一

def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)
print(fib(10))

# 方法二

def fib(n):
    a, b = 1, 1
    for i in range(n - 1):
        a, b = b, a+b
    return a
print(fib(10))

# 输出结果

55
