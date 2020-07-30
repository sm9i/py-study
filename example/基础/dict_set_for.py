# -*- coding: utf-8 -*-


# 字典 类似java的map key-value
# key 为不可变对象

dic = {'name': 'wangyi', 'age': 18, 'sex': 1}
print(dic['name'])

# 动态赋值
dic['school'] = 'beidaqingN'

print(dic)

# 是否存在用in 或者 get

if 'name' in dic:
    print('name 存在')
else:
    print('name 不存在')

print(dic.get('oo', ' oo 不存在'))

# 删除使用pop
dic.pop('sex')
print(dic)

# dict 查 插 速度快
#      占用内存大
# list 查 插 和元素成正比
#      空间小 内存小


# set 不重复的list

print('--------------------------')

# 需要一个list输入 可去重复
s = set([1, 2, 3, 1, 4])
print(s)
s.add(0)
s.remove(1)
print(s)
# 无须和无重复的集合 可以做交并集等操作
s2 = set([1, 2, 3])
print(s & s2)
print(s | s2)

print('--------------------------')

# 循环

names = ['job', 'any', 'tom']
for name in names:
    print(name)

n = 0
for i in range(101):
    n += i
print(n)

a = 0
count = 99
while count > 0:
    a = a + count
    count = count - 2
print(a)

l_name = ['Bart', 'lisa', 'Adam']
for na in l_name:
    print('hello, %s' % na)

# break continue
