"""输入：hello nowcoder
输出：8
说明：最后一个单词为nowcoder，长度为8

也可以使用指针 逆序for循环 直至空格

"""

import sys

for line in sys.stdin:
    a = line.split()
    l = len(a)
    last_word = a[l - 1]
    print(len(last_word))

# a = input()
# l = len(a)
# last_word = a[l - 1]
# print(len(last_word))
