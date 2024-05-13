x = [2, 4, 6]
i = x.__iter__()
print(i)
print(i.__next__())
print(i.__next__())

print(str(i.__next__()) + 'a')


def collatz(n):
    while n != 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = 3 * n + 1
        yield n  # 使用return的话：  TypeError: 'int' object is not iterable


for x in collatz(7):
    print(x)

i = collatz(3)
print(i)
print(i.__next__())
print(i.__next__())
print(i.__next__())
print(i.__next__())
print(i.__next__())
print(i.__next__())
print(i.__next__())
print(i.__next__())
print(i.__next__())  # None
