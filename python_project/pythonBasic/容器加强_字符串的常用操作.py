import sys
from random import random, randint, shuffle
from math import floor, ceil, exp, fabs, log
sys.stdout.write('Hello python\n')

# python数据类型之间的转换
# repr()    将对象 x 转换为表达式字符串
# eval(str)   用来计算在字符串中的有效Python表达式,并返回一个对象
# chr(x)    将一个整数转换为一个字符
# ord(x)    将一个字符转换为它的整数值
# hex()     将一个整数转换为一个十六进制字符串
# oct()     将一个整数转换为一个八进制字符串

s = 'A'
print(ord(s))

a = 97
print(chr(a))

def func():
    """
    这是注释
    :return:
    """
    pass

print(func.__doc__)  # 输出函数注释

a = 1
b = 1
print(a is b)


"""
字符串是 Python 中最常用的数据类型。我们可以使用引号( ' 或 " )来创建字符串。
"""
a = 'hello\t'
b = 'python'
print(a + b)

print(floor(randint(1, 10)))
l = [i for i in range(1, 10)]

print(l)

shuffle(l)
print(l)
print(sorted(l))
print(l, a)

d = {'a': 12, 's': 6, 'c': 4}
print(sorted(d))


def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    return fibonacci(n-1)+fibonacci(n-2)

def fiboArray(n):
    for i in range(1, n+1):
        yield fibonacci(i)
a = fiboArray(10)
for i in range(10):
    print(next(a))

