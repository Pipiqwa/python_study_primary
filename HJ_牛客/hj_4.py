"""
字符串切分 分割 分隔
"""
while True:
    try:
        a = input()

        while len(a) > 8:
            b = a[:8]
            print(b)
            a = a[8:]
        else:
            c = a + (8-len(a)) * '0'
            print(c)
    except:
        break
