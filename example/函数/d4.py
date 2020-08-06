# 返回函数


# 求和 立即返回值
def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax


print(calc_sum(1, 2, 3, 4))


# 求和 返回方法  调用的时候才会返回
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax

    return sum


print(lazy_sum(1, 3, 4, 4))
print(lazy_sum(1, 3, 4, 4)())


# 执行 等执行的时候 i=3 了 所以都是  9
def count():
    fs = []
    for i in range(1, 4):
        def f(): return i * i

        fs.append(f)
    return fs


f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())


# 闭包 返回函数不要引用任何循环变量  或者后续发生变化的值
# 解决办法是 创建一个新函数 用参数绑定 当前循环的变量
def count():
    def f(j):
        def g(): return j * j

        return g

    fs = []
    for i in range(1, 4):
        fs.append(f(i))
    return fs


f1, f2, f3 = count()
# 正常
print(f1())
print(f2())
print(f3())


# 计数器
def createCount():
    n = 0;

    def counter():
        nonlocal n
        n += 1
        return n

    return counter


count = createCount()
print(count())
print(count())
print(count())
