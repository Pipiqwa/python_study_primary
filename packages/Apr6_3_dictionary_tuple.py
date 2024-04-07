# tuple 元组
a = [(1, 3), 3, 5]
print(a)

# File IO
# f = open('data.txt', 'w')
# f.write('1 2 3 4\n')
# f.write('2 3 4 5\n')
# f.close()

# 字典
contacts = {"小明": "12345678900",
            "小花": "12300000000"}

contacts["小小"] = "0000000000"

print("小明" in contacts)

# 删除一个键值对
del contacts["小明"]

contacts = {'张三': '123456', '李四': '789012', '王五': '345678'}

while True:
    arg = input("添加还是查询？（0为添加，1为查询）")
    if arg == '0':
        name = input("输入要添加的姓名：")
        phone = input("输入" + name + "的电话号码：")
        contacts[name] = phone
        print("添加成功!")
    elif arg == '1':
        query = input("输入要查询的姓名：")
        if query in contacts:
            print("您查询'" + query + "'的电话为")
            print(contacts[query])
        else:
            print("联系人不在通讯录内")
            print("当前通讯录已存条数:" + str(len(contacts)))
    else:
        print("输入有误,请重新输入")
        continue
# while input("添加还是查询？（0为添加，1为查询）") != None:
#     pass