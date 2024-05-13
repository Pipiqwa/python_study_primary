"""
输出字符串内出现的字符的次数（不区分大小写）
输入：
ABCabc
A
输出：
2
"""

import sys

new_line = ''
i = 0
char_dict = {}

for line in sys.stdin:
    if i == 0:
        for char in line:
            if char.isupper():
                char = char.swapcase()
            new_line += char

        for char in new_line:
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1

        i += 1
    else:
        if line.isupper():
            line = line.swapcase()

        try:
            print(char_dict[line[:-1]])
        except KeyError:
            print('0')


        char_dict = {}
        i = 0
        new_line = ''

