# 比我写的快 呜呜
import math
n = int(input())
for i in range(2, int(math.sqrt(n))+1):
    while n % i == 0:
        print(i, end=' ')
        n = n // i   # 整除 返回int
if n > 2:
    print(n)
