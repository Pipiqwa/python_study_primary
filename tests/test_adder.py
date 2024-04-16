"""
可以在终端cd tests过来
使用命令
py -m unittest
"""
import unittest
from packages.Apr8_3_assert import my_adder

class TestMyAdder(unittest.TestCase):
    def test_positive_with_positive(self):
        assert my_adder(5, 3) == 8


    def test_negative_with_positive(self):
        self.assertEquals(my_adder(-5, 3), -2)

    @unittest.skip
    def test_negative_with_negative(self):
        self.assertEquals(my_adder(-5, -4), -9)

    def setUp(self):  # 使用setUp 设定预设 my_add
        self.my_add = my_adder(0,10)

    def test_0_plus_100(self):
        self.assertEquals(self.my_add,11)

