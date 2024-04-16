# File IO  '../' 访问上级direction  ./ 会找当前目录 不加./ 效果一样
f = open('./data.txt', 'w', encoding="utf-8")
f.write('0 2 3 4\n')
f.write('2 3 4 5\n')

f = open('../files/data.txt', 'w', encoding="utf-8")
f.write('1 2 3 4\n')
f.write('2 3 4 5\n')

f = open('C:/Users/pipiqwq/PycharmProjects/pythonProject_0/files/data_0.txt', 'a+', encoding="utf-8")
f.write('1 2 3 4\n')
f.write('00000000')
print(f.read())   # a+

f.close()  # 释放系统资源

f = open('C:/Users/pipiqwq/PycharmProjects/pythonProject_0/files/data_0.txt', 'r', encoding="utf-8")
print(f.read())

f.close()

f = open('C:/Users/pipiqwq/PycharmProjects/pythonProject_0/files/data_0.txt', 'r', encoding="utf-8")
lines = f.readlines()
for line in lines:
    print(line[:-1])  # 删除最后一个字符

# 使用with 不需要 close
with open('data.txt', 'r', encoding="utf-8") as f:
    print(f.read(11))  # 只读多少个字符 （换行不算入）
