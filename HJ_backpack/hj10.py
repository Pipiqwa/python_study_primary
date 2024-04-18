"""
字符串统计个数
"""
a = 'abc'
b = ''
n = 0
for char in a:
    if char not in b:
        b += char

print(b)

c = set(a)
print(len(c))

x = 'G'
print(ord(x))   # ord 输出字符的 acsii 码   Return the Unicode code point for a one-character string.