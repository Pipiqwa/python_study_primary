import sys

can_sort = False
a = 0
lst = []
for line in sys.stdin:
    if not can_sort:
        a = int(line)
        can_sort = True
    else:
        if a >= 1:
            lst.append(line)
            a -= 1
            if a == 0:
                print(''.join(sorted(lst)))
                lst = []
                can_sort = False

