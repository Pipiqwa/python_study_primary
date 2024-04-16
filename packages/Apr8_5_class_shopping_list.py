class ShoppingList:
    def __init__(self, shopping_list):
        self.shopping_list = shopping_list

    def __setitem__(self, key, value):
        self.shopping_list[key] = value  # 将键值对添加到字典中

    def __getitem__(self):
        return self.shopping_list  # 如果需要，也可以定义 __getitem__ 方法来获取字典

    def add_item(self, name, amount):
        self.shopping_list[name] = amount  # 使用字典 数据结构

    def query_amount_by_name(self, name):
        return self.shopping_list[name]

    def query_item_count(self):
        return len(self.shopping_list)

    def query_total_price(self):
        total_price = 0
        for num in self.shopping_list.values():  # 字典的 值
            total_price += num
        return total_price

    def values(self, key):
        return self.shopping_list[key]


shopping_list1 = ShoppingList({"牙刷": 5})
shopping_list1.add_item('牙刷', 5)
shopping_list1["帽子"] = 13

dict_0 = {"鞋子": 1, '3': 12}
print(dict_0['3'])

for val in shopping_list1.__dict__.values():
    print(val)

print(shopping_list1.__dict__.values())

if __name__ == '__main__':
    pass




class MyClass:
    def __init__(self):
        self.a = 1
        self.b = 2
        self.c = 3


# 实例化类
my_instance = MyClass()

# 直接迭代 __dict__ 属性
for value in my_instance.__dict__.values():
    print(value)
print(my_instance.__dict__.values())


import json  # dump 转存
print(json.dumps(list(my_instance.__dict__.values()), indent=4))