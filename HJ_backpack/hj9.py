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
#print(c)
print(d)
