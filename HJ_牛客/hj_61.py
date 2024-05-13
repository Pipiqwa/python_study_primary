# This is file hj_61.py    HJ61 放苹果
"""
把m个同样的苹果放在n个同样的盘子里，允许有的盘子空着不放，问共有多少种不同的分法？
注意：如果有7个苹果和3个盘子，（5，1，1）和（1，5，1）被视为是同一种分法。

1≤ n or m ≤10

输入描述：
输入两个int整数

输出描述：
输出结果，int型

输入：
7 3

输出：
8
"""

a = list(map(int,input().split()))
m = a[0]
n = a[1]

def dfs(x,y):  # x apple   y dish
    if x != 0:
        pass
    pass

dfs(m,n)


