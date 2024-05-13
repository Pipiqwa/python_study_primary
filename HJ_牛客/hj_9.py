"""
提取不重复的整数
"""

a = input()
b = len(a)
c = []
for i in range(0,b):
    if a[i] not in c:
        c.append(a[i])

c.sort()
d = ''.join(map(str,c))
print(d)


"""
从后往前读(右边 -》 左边)
9876673
37689
"""

a = input()
b = len(a)
c = []
for i in range(0,b):
    if a[b-i-1] not in c:
        c.append(a[b-i-1])


d = ''.join(map(str,c))
print(d)
