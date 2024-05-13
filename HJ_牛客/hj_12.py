# 字符串反转  必须是小写字母
a = input()
# a = 'az'

b = a[::-1]
print(b)


c = ''
bool_all_lower = True
for char in a:
    b = ord(char)
    if 97<=ord(char)<=122:
        c = char + c
    else:
        bool_all_lower = False
        break

if bool_all_lower:
    print(c)