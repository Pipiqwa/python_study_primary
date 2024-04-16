# tuple 元组(1,3)
a = [(1, 3), 3, 5]
print(a)

# 字典
contacts = {"小明": "12345678900",
            "小花": "12300000000"}

# contacts["小小"] = "0000000000"

print("小明" in contacts, "\n")

# 删除一个键值对
del contacts["小明"]

contacts = {'张三': '123456', '李四': '789012', '王五': '345678'}

arg = input("添加还是查询？（0为添加，1为查询,q为退出,随时按b为回到主菜单）")
while arg is not None:
    if arg == 'b':
        arg = input("添加还是查询？（0为添加，1为查询,q为退出,随时按b为回到主菜单）")
        continue

    if arg == '0':
        name = input("输入要添加的姓名：")
        if name == 'b':
            arg = input("添加还是查询？（0为添加，1为查询,q为退出,随时按b为回到主菜单）")
            continue

        phone = input("输入" + name + "的电话号码：")
        if phone == 'b':
            arg = input("添加还是查询？（0为添加，1为查询,q为退出,随时按b为回到主菜单）")
            continue

        contacts[name] = phone
        print("添加成功!")
        arg = input("添加还是查询？（0为添加，1为查询,q为退出,随时按b为回到主菜单）")

    elif arg == '1':
        query = input("输入要查询的姓名：")
        if query == 'b':
            arg = input("添加还是查询？（0为添加，1为查询,q为退出,随时按b为回到主菜单）")
            continue
        if query in contacts:
            print("您查询'" + query + "'的电话为")
            print(contacts[query])
            arg = input("添加还是查询？（0为添加，1为查询,q为退出,随时按b为回到主菜单）")
        else:
            print("联系人不在通讯录内")
            print("当前通讯录已存条数:" + str(len(contacts)))
            arg = input("添加还是查询？（0为添加，1为查询,q为退出,随时按b为回到主菜单）")

    elif arg == 'q':
        print("程序现在退出")
        break

    else:
        print("输入有误,请重新输入")
        arg = input("添加还是查询？（0为添加，1为查询,q为退出,随时按b为回到主菜单）")
        continue
# while input("添加还是查询？（0为添加，1为查询）") != None:
#     pass
