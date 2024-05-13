listdemo = ['Google','Runoob', 'Taobaoooo']
# 将列表中各字符串值为键，各字符串的长度为值，组成键值对
newdict = {key:len(key) for key in listdemo}
{'Google': 6, 'Runoob': 6, 'Taobao': 6}
print(newdict)
print(id(newdict))
squares = [x**2 for x in range(10)]  # 创建一个包含0到9的平方的列表