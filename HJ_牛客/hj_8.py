"""
输入：
4
0 1
0 2
1 2
3 4

输出：
0 3
1 2
3 4
"""

a = int(input())
b_dict = {}
for i in range(0, a):
    c = list(map(int, input().split()))
    if c[0] not in b_dict:
        b_dict[c[0]] = c[1]
    else:
        b_dict[c[0]] = b_dict[c[0]] + c[1]



for key in sorted(b_dict):
    print(key,b_dict[key])

a = 1
b = 2
print(a,b)

{print(f'Key: {k}, Value: {v}') for k, v in b_dict.items()}