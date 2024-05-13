import sys

the_line = ''
the_character = ''
i = 0
total = 0

for line in sys.stdin:
    if i == 0:
        the_line = line.lower()
        i += 1
    else:
        the_character = line.lower()
        i = 0

        for char in the_line:
            if char == the_character[:-1]:
                total += 1

        print(total)
        total = 0
