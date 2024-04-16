"""
输出字符串内出现的字符的次数（不区分大小写）
输入：
ABCabc
A
输出：
2
"""

import sys

i = 0
char_dict = {}

for line in sys.stdin:
    if i == 0:
        for char in line:
            if char in char_dict:
                if char in "ABCD":
                    char.
                char_dict[char] += 1
            else:
                char_dict[char] = 1
        i += 1
    else:
        print(char_dict[line[:-1]])
        char_dict = {}
        i = 0
