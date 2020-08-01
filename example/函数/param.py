# -*- coding: utf-8 -*-

# 默认参数 可不赋值
# 默认参数必须指向不变对象！
def power(x, y=2):
    return x * y


# 必选参数必须在前

print(power(2))
print(power(2, 4))
# 不按照顺序 直接指定参数名
print(power(2, y=4))


# 参数必须是不可变对象
def add_end(l=None):
    return l


# 可变参数
def cale(*number):
    return number


print(cale(10, 2))

# 可变参数允许传入0+ 自动转为tuple
print(cale(*[1, 2, 3, 4]))


# 关键字参数
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


# 关键词参数 自动转为dict
# src 为关键字参数
print(person('Jok', 19, src=3, school=2222))

extra = {'city': 'sh', 'c_code': 20000}


# 关键字参数可以传入一个dict 作为默认
def person_1(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
    pass


print(person_1('Jok', 19, **extra))


# 命名关键字参数 表示 关键字参数只接受  job 和city
# if 'city' int kw 关键字中有city
#
#
def person_2(name, age, *, job, city):
    print(name, age, city, job)


# 关键字参数必传否则报错
# person_2('22', 1)

# 如果有一个可变参数了 只需要一个 *
# 并且 args 可以为null  * 就好了
def person_3(name, age, *args, job, city='有默认值可以不传递'):
    print(name, age, city, job, args)


# 默认参数
person_3('22', 1, '22222', job='sh', city='shh')
person_3('22', 1, '22222', job='sh')

# 顺序  必选 - 默认 - 可变 - 命名关键字
#
# Python的函数具有非常灵活的参数形态，既可以实现简单的调用，又可以传入非常复杂的参数。
#
# 默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误！
#
# 要注意定义可变参数和关键字参数的语法：
#
# *args是可变参数，args接收的是一个tuple；
#
# **kw是关键字参数，kw接收的是一个dict。
#
# 以及调用函数时如何传入可变参数和关键字参数的语法：
#
# 可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；
#
# 关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。
#
# 使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。
#
# 命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。
#
# 定义命名的关键字参数在没有可变参数的情况下不要忘了写分隔符*，否则定义的将是位置参数。
