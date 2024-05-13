# 给你一个数5，求它的二进制（binary）的1的出现的次数   题目：求int型正整数在内存中存储时1的个数

b = bin(11937197)
c = b[1:].count('1')
print(c)

a = '101010010001001001'
print(bin(int(a)).count('1'))