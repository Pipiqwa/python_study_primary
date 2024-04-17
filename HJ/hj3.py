"""
輸入3
23
34
56
輸出這順序3個數字
"""

import sys

i = 0
time = 0
l = []
for line in sys.stdin:
    num = int(line)
    if i == 0:
        try:
            i += 1
            time = num
        except:
            print("0")

    else:
        if num not in l:
            l.append(num)
        i += 1
        if i == time+1:
            l.sort()
            print(l)
            for n in l:
                print(n)
            i = 0
            time = 0
            l = []





