# This is file hj_21.py  HJ21 简单密码
"""
九键手机键盘上的数字与字母的对应：
1--1， abc--2, def--3, ghi--4, jkl--5, mno--6, pqrs--7, tuv--8 wxyz--9, 0--0，
把密码中出现的小写字母都变成九键键盘对应的数字，
如：a 变成 2，x 变成 9.
而密码中出现的大写字母则变成小写之后往后移一位，如：X ，先变成小写，再往后移一位，变成了 y ，例外：Z 往后移是 a 。
输入描述：
输入一组密码，长度不超过100个字符。
输入：
YUANzhi1987

输出描述：
输出密码变换后的字符串
输出：
zvbo9441987
"""
a = input()
# a = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
c = ''


switcher = {
    'a': 2, 'b': 2, 'c': 2,
    'd': 3, 'e': 3, 'f': 3,
    'g': 4, 'h': 4, 'i': 4,
    'j': 5, 'k': 5, 'l': 5,
    'm': 6, 'n': 6, 'o': 6,
    'p': 7, 'q': 7, 'r': 7, 's': 7,
    't': 8, 'u': 8, 'v': 8,
    'w': 9, 'x': 9, 'y': 9, 'z': 9,
}

low = 'abcdefghijklmnopqrstuvwxyz'  # pyhon的字符串存储就是list，可以直接用list的方法，没必要转换一下。
num = '22233344455566677778889999'

if len(a) > 100:
    pass
# else:
#     for i in a:
#         o_i = ord(i)  # 转 Unicode code point
#         b[i] = o_i
#         if 64 < o_i < 90:  # 大写字母
#             c += chr(o_i + 1).lower()
#         elif 96 < o_i < 122:  # 小写字母
#             c += str(switcher[i])
#         elif 47 < o_i < 58:  # 数字
#             c += chr(o_i)
#         else:
#             c += i
else:
    for i in a:
        if i.isupper():  # 大写字母
            if i == 'Z':
                c += 'a'
            else:
                c += chr(ord(i) + 1).lower()
        elif i.islower():  # 小写字母
            # c += str(switcher[i])
            c += num[low.index(i)]
        else:
            c += i

# print(sorted(b.items()))
# # 对元组排序会按照先后元素依次排序
# print(sorted([(1, 'ca'), (1, 'abd'), (1, 'bcd')]))

print(c)
