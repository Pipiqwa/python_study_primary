"""   洛谷点位测试？
要放在主目录下
要 test 命名开头
在终端输入：
py -m unittest
"""
import unittest

from packages.Apr8_3_assert import my_adder


class TestMyAdder(unittest.TestCase):
    def test_positive_with_positive(self):
        assert my_adder(5, 3) == 8
        self.assertTrue(2 not in [1, 3, 4])

        self.assertIn(2, [1, 5, 3])
        """ 可以给出详细失败原因"""

    def test_negative_with_positive(self):
        self.assertEquals(my_adder(-5, 5), 0)

    # @unittest.skip
    def test_negative_with_negative(self):
        self.assertEquals(my_adder(-5, -4), -9)

    def test_positive_with_negative(self):
        self.assertEquals(my_adder(5, -5), 0)


"""
assertTrue(A)
assertIn(A,B)

assertNotEqual(A,B)


"""

# if __name__ == '__main__':
#     unittest.main()
