# 取近似值

#思路1

# from math import ceil,floor
# def ceilNumber(n):
#     a = ceil(n)-n
#     if (a<=0.5):
#         return ceil(n)
#     return floor(n)
# b = float(input())
# print(ceilNumber(b))


#思路2
# def ceilNumber(n):
#     a = int(n+0.5)
#     return a
# b = float(input())
# print(ceilNumber(b))

#思路3
n = float(input())
y = lambda x: int(x+0.5)
print(y(n))

"""
第 七 题 对照
"""
"""
import math
num = int(input())
s = ''
prime = 2
while prime < math.sqrt(num)+1:
    if num%prime != 0:
        prime += 1
    else:
        num = num //prime
        s += str(prime)+' '
        prime = 2
if num>=2:
    s += str(num)+' '
print(s)
"""

"""
第八题
四舍五入
"""
a = float(input())
b = a % 1
c = a - b
if b >= 0.5:
    c = c+1
print(int(c))
