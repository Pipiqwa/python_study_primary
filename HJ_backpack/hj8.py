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