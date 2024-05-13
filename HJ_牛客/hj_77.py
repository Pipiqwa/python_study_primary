# This is file hj_77.py   火车进站

"""
知识点
栈


给定一个正整数N代表火车数量，0<N<10，接下来输入火车入站的序列，一共N辆火车，每辆火车以数字1-9编号，火车站只有一个方向进出，同时停靠在火车站的列车中，只有后进站的出站了，先进站的才能出站。
要求输出所有火车出站的方案，以字典序排序输出。

输入描述：
第一行输入一个正整数N（0 < N <= 10），第二行包括N个正整数，范围为1到10。

输出描述：
输出以字典序从小到大排序的火车出站序列号，每个编号以空格隔开，每个输出序列换行，具体见sample。
"""

'''
甲乙丙丁戊 己庚辛壬癸

子丑寅卯辰已
午未申酉戌亥
'''
"""
4:
1 2 3 4
12 3 4
123 4

1 23 4
1 234

1 2 34

9:
1 2 3 4 5 6 7 8 9
12 3 4 5 6 7 8 9
123 4 5
1234 5

1 23 4 5
1 234 5
1 2345


"""
res = []

def dfs(wait, stack, out):
    if not wait and not stack:
        res.append(' '.join(out))
    if wait:  # 入栈
        dfs(wait[1:], stack + wait[0], out)
    if stack:  # 出栈
        dfs(wait, stack[:-1], out + stack[-1])


a = int(input())
b = ''
for i in range(1, a + 1):
    b += str(i)

wait = b
stack = ''
out = ''

dfs(wait, stack, out)

for i in sorted(res):
    print(i)
