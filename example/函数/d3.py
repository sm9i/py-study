# 函数可以作为变量 那也可以作为参数
from functools import reduce


# 高阶函数

# f作为方法
def add(a, b, f):
    return f(a) - f(b)


print(add(2, 3, abs))


# map 、reduce
# map 接收一个 方法 一个 是Iterable

def f(s):
    return s * s


R = map(f, range(5))
print(list(R))

# 把0-10数字转为字符串
print(list(map(str, range(10))))


# reduxe 接收一个方法 和一个集合
# 会吧 前两个计算的结果和后一个继续计算


def a_sum(x, y):
    return x - 1 + y


f = reduce(a_sum, [1, 3, 4])
print(f)

# 练习

L1 = ['adam', 'LISA', 'barT']


def normalize(name):
    name = name.lower()
    return name.replace(name[0], name[0].upper(), 1)


L2 = list(map(normalize, L1))
print(L2)

print(normalize('Lis'))


# reduce 求积

def prod(x, y):
    return x * y;


print(reduce(prod, [3, 5, 7, 9]))

# str 2 float


DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


# 吧str转为s
def str2num(s):
    return DIGITS[s]


print('-----')


def str2float(s):
    s1 = s.split('.')[0]
    s2 = s.split('.')[1]
    print(s1)
    print(s2)
    x1 = reduce(lambda x, y: x * 10 + y, map(str2num, s1))
    print(x1)
    x2 = reduce(lambda x, y: x / 10 + y, map(str2num, s2[::-1])) / 10
    print(x2)
    return x1 + x2


print('str2float(\'123.456\') =', str2float('123.456'))
