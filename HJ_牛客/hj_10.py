"""
字符串统计个数
"""
a = 'abc'
a = input()
b = ''

for char in a:
    if char not in b:
        b += char

print(b)
c = set(a)
print(len(c))

x = '\n'   # 97~122  a~b     65~90 A~Z
print(ord(x))   # ord 输出字符的 acsii 码   Return the Unicode code point for a one-character string.