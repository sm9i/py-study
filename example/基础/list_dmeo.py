# -*- coding: utf-8 -*-


# list 
classmates = ['a', 'b', 'c']
# 下标获取
print(classmates[0])
print(classmates[1])

print('len()获取list长度 %d' % len(classmates))

# 直接获取最后一个可以用 -1


print(classmates)
# 追加使用append
classmates.append('add')

print('追加后的 %s' % classmates)

# 插入使用insert
classmates.insert(2, 'insert')
print('插入后的 %s' % classmates)

# 删除用pop 传递index  不传默认最后一个
classmates.pop(2)
print('删除后的 %s' % classmates)
# 替换直接传递i
classmates[1] = 'aaa'
print('替换后的 %s' % classmates)
