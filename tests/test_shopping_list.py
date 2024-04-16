import unittest
from packages.Apr8_5_class_shopping_list import ShoppingList


class TestShoppingList(unittest.TestCase):
    def setUp(self):
        shopping_list0 = ShoppingList({})  # 实例化 记得加() 以及输入该类需要的属性（值）
        shopping_list0.add_item('牙刷', 5)
        shopping_list0["帽子"] = 13
        self.list = shopping_list0

    def test_query_amount_by_name(self):
        self.assertEqual(self.list.query_amount_by_name("牙刷"), 5,"查询结果不符.")

    def test_query_total_price(self):
        self.assertEqual(self.list.query_total_price(), 18)


