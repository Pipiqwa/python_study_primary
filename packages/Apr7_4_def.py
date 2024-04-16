a = [1, 2, 3]
a.append(7)
print(a)

# append函数 没有返回值 返回None
b = [1, 2, 3].append(7)
print(b)
print('\n')

print(sum(a) + sum([0, -1, -2]))
print('\n')

# 迭代
list_0 = [1, 2, 3, 4]
it = iter(list_0)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print('\n')

# !/usr/bin/python3

list_1 = [1, 2, 3, 4]
it = iter(list_1)  # 创建迭代器对象
str_0 = ''
for x in it:
    print(x, end=" ")
    str_0 += str(x)
    str_0 += str(' ')
print('\n')

str_1 = '12345678'
print(str_1[1:])  # 去掉多少
print(str_1[:1])  # 保留多少
