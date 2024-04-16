"""
整数	-100
浮点数	3.1416
字符串	'hello'
列表	[1, 1.2, 'hello']
字典	{'dogs': 5, 'pigs': 3}
| 长整型 | 1000000000000L |
布尔型 | True, False |
元组 | ('ring', 1000) |
集合 | {1, 2, 3} |
Pandas类型| DataFrame, Series |
自定义 | Object Oriented Classes
"""

set1 = {1, 2, 3, 4}   # set 集合

shopping_list = ["键盘", "键帽", "键帽", "音响", 123]
print(shopping_list)

price = [799, 1024, 200, 800]
max_price = max(price)
min_price = min(price)
sorted_price = sorted(price, key=lambda x: x * -1)

print(len(price))
print(sorted_price)


def get_negative(value):  # 使用普通函数作为key
    return -value


sorted(price, key=get_negative)


class Product:  # 使用属性作为 key 参数：
    def __init__(self, _id, name, p_price):
        self.id = _id
        self.name = name
        self.price = p_price


products = [Product(1, "hammer", 9.99),
            Product(2, "screwdriver", 4.99),
            Product(3, "wrench", 15.99)]

sorted_products = sorted(products, key=lambda x: x.price)   # 排序 输入第一个对象products，  排序key  为 输入对象的 属性
print([p.name for p in sorted_products])  # 输出: ['screwdriver', 'hammer', 'wrench']

