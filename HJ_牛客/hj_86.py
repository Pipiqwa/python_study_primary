# This is file hj_86.py   求最大连续bit数
"""
知识点
位运算

输入描述：
输入一个int类型数字

输出描述：
输出转成二进制之后连续1的个数

输入：
200
输出：
2

说明：
200的二进制表示是11001000，最多有2个连续的1。
"""
a = int(input())
b = bin(a)
c = oct(a)
d = hex(a)

n = 0
n_max = 0

left = 0
right = len(str(b))

print(b,c,d)

for i in range(right):
    if b[i] == '1':
        n += 1
        if n > n_max:
            n_max = n
    else:
        n = 0
print(n_max)


x = int(input())
byte_x = bin(x)[2:]
list1 = sorted(list(set(byte_x.split('0'))), key = lambda x: len(x), reverse=True)  # 按list内元素的（字符串）长度排序，倒序
print(len(list1[0]))


# 这个写法最牛逼
a = bin(int(input()))
b = str(a)
for i in range(len(a)):
    if '1' * (len(a) - i) in b:
        print(len(a) - i)
        break
