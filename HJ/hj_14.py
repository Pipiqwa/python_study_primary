# 字符串排序
"""
输入：
9
cap
to
cat
card
two
too
up
boat
boot

输出：
boat
boot
cap
card
cat
to
too
two
up
"""

n = int(input())
stack = []

for i in range(0,n):
    stack.append(input())

stack.sort()

print("\n".join(stack))