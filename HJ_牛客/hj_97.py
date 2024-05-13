# This is file hj_97.py  记负均正
"""
输入：
11
1 2 3 4 5 6 7 8 9 0 -1

输出：
1 5.0
"""

a = int(input())
b = list(map(int, input().split()))

# print(a)
# print(b)

c = 0
d = 0
for n in b:
    if n < 0:
        c += 1
    else:
        d += n

e = d / (a - c)

# print(c)
# print(e)
print(f"{c} {e}")
