# 明明的随机数

a = int(input())
b = []
for i in range(0, a):
    c = int(input())
    if c not in b:
        b.append(c)
# b.sort()  # list（序列）才可以sort  sort
# b = sorted(b)  # 因为是 str 所以按照 字符序码 排序

d = sorted(b)
# b = [1,2,3]
# print(d)

print("\n".join(map(str,d)))
