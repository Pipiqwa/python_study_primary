"""
确保在包含测试脚本的目录中运行 python -m unittest 命令
使用 python -m unittest your_test_script.py 明确指定测试文件的名称。
检查您的测试文件和类名是否符合 unittest 的命名约定。
确保所有依赖模块都在 PYTHONPATH 环境变量中正确设置。
"""

"""
unittest 默认会搜索当前目录下所有以 test 开头的文件和类。
如果您的测试文件或类名不符合这个约定，unittest 将无法发现它们。
请检查您的文件名是否以 test 开头，
并且类名以 Test 开头。
"""
import unittest
from Apr8_3_assert import my_adder

class TestMyAdder(unittest.TestCase):
    def test_positive_with_positive(self):
        assert my_adder(5, 3) == 8


    def test_negative_with_positive(self):
        self.assertEqual(my_adder(-5, 3), -2)

    @unittest.skip
    def test_negative_with_negative(self):
        self.assertEqual(my_adder(-5, -4), -9)

