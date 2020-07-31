# -*- coding: utf-8 -*-
import math

print(type(int('123')))
print(type(float('123')))
print(type(bool('123')))

# 方法可以赋值给变量
a = abs
print(a(-2.2))

print(hex(9))


# 求绝对值
def my_abs(x):
    # 参数的类型只能为 int 和 float
    if not isinstance(x, (int, float)):
        raise TypeError('类型不对')
    if x > 0:
        return x
    else:
        return -x


# 空函数
def nop():
    pass


# 多值返回其实是一个 tuple
def more_return(x, y):
    return x + y, x - y
    pass


print(my_abs(-10))
# print(my_abs('22'))
print(more_return(1, 4))
print('多返回值类型 %s' % type(more_return(1, 2)))


# ax²+bx+c=0
def quadratic(a, b, c):
    return (-b + math.sqrt(b ** 2 - 4 * a * c)) / 2 * a, (-b - math.sqrt(b ** 2 - 4 * a * c)) / 2 * a
    pass


print(quadratic(1, 44, 2))
