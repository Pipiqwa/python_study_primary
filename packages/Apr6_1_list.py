
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

sorted_products = sorted(products, key=lambda x: x.price)
print([p.name for p in sorted_products])  # 输出: ['screwdriver', 'hammer', 'wrench']

