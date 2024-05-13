"""
質數因子

21820189210
2 5 2182018921

2182018921

2182018922
2 61 257 69593

237623686181212
2 2 53 1120866444251
"""
import math

while True:
    a = int(input())
    a_backup = a
    n = 2
    prime_lst = [1]

    while a != 1:
        remainder = a % n
        if remainder == 0:
            a = a / n
            if a != 1:
                print(n, end=' ')
            else:
                print(n)
                break  # 刚好被整除了 结束   可以break 也可以不加
            # prime_lst.append(n)
        else:
            n += 1
            # if n == a:
            if n > math.sqrt(a_backup) or n > a:  # 当 n 增加到 大于a的 开方时，肯定的就是，a已经不能被除了，除了自己作为除数
                print(int(a))  # 所以此时 输出 a 即可
                # prime_lst.append(n)
                break
    else:
        print(1)
    # print(prime_lst)
    # print(str(prime_lst[1:]))

    # 使用列表记录
    # sss_lst = prime_lst[1:]
    # print(' '.join(map(str, sss_lst)))
