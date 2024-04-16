import sys

i = 0
time = 0
l = []
for line in sys.stdin:
    if i == 0:
        try:
            i += 1
            time = int(line)
        except:
            print("0")

    else:
        if line not in l:
            l.append(int(line))
        i += 1
        if i == time+1:
            l.sort()
            print(l)
            for n in l:
                print(n)
            i = 0
            time = 0
            l = []





