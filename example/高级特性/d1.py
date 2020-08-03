# -*- coding: utf-8 -*-

# from collections import Iterable
import os

# 切片 slice

L = ['jok', 'andy', 'tom', 'tony']

print('取 0-3 %s' % L[0:3])
print('取 1-3 %s' % L[1:3])

# [x:y] 从x开始到y为止  但不包括y
# 如果x是0 还可以省略
print('取 0-3 %s' % L[:3])

# 支持倒数  x为-1
print('取 0-3 %s' % L[-2:])

num_L = list(range(100))

print('取11-20 %s' % num_L[10:20])
print('取0-20每两个一次 %s' % num_L[:20:2])
print('所有数字每5个一次 %s' % num_L[::5])

# 复制list [:]
# tuple ,str也可以用切片

# 迭代
for k, v in {'a': 1, 'b': 1, 'c': 1, 'd': 1}.items():
    print(k, v)

# print('判断是否可迭代 %s' % isinstance('abc', Iterable))
# print('判断是否可迭代 %s' % isinstance(123, Iterable))

# enumerate 可以把list变为 有下标的


# 列表生成
l1 = [x * x for x in range(1, 11)]
l2 = [x * x for x in range(1, 11) if x % 2 == 0]
l3 = [x + y for x in 'abc' for y in 'xyz']
print(l1)
print(l2)
print(l3)
l4 = [d for d in os.listdir('.')]
print('%s' % l4)

# for 前面的if else 是表达式  后面的是过滤条件不能带else

# 一边循环一边计算后续  generator

print([x * x for x in range(10)])  # list
g = (x * x for x in range(10))
print(g)
print(next(g))
print(next(g))

# 也可以循环generator
for n in g:
    pass

# yield
print('####################')


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


fib(20)

# 如果一个函数中有yield 那这个函数就是个generator

f = fib(6)
print(f)


def odd():
    print('step 1')
    yield 11
    print('step 2')
    yield 22
    print('step 3')
    yield 33


o = odd()
print(next(o))
print('-')
print(next(o))
print('-')
print(next(o))
# generator 在遇到 yield 的时候回返回 下次执行会 继续从这执行


# for 循环 generator 拿到返回值必须用 StopIteration
g = fib(6)
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('return value ', e.value)
        break


# 杨辉三角 牛逼
def sj():
    L = [1]
    while True:
        yield L
        S = L[:]
        S.append(0)
        L = [S[i - 1] + S[i] for i in range(len(S))]


a = sj();
for i in range(10):
    print(next(a))
