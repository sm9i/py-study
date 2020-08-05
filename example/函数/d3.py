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

print('------')


# filter 用于过滤 筛选  类似 where


# 保留奇数
def is_odd(n):
    return n % 2 == 1


print(list(filter(is_odd, range(10))))


# 奇数数列 生成器
def _off_iter():
    n = 1
    while True:
        n = n + 2
        yield n


# 筛选 如果 x 和n求余 大于 0 就保留

def _not_divisible(n):
    return lambda x: x % n > 0


def primes():
    yield 2
    it = _off_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)


# 1000 内的所有素数
for n in primes():
    if n < 1000:
        print(n)
    else:
        break


# 求回数  反向然后和原数比较 秀
def is_palindrome(n):
    return int(str(n)[::-1]) == n


print(list(filter(is_palindrome, range(55, 1000))))

# 排序
# key 类似一个数据处理
# reverse 是否 倒叙
a = sorted([323, 5342, 4534, -4534, -23], key=abs, reverse=True)
print(a)

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


# 按名字排序
def by_name(t):
    return t[0]


def by_score(t):
    return t[-1]


print(sorted(L, key=by_name))
print(sorted(L, key=by_score))
