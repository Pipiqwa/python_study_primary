class Solution:
    def reverseMessage(self, message: str) -> str:
        return ' '.join(message.split()[::-1])

class Solution0:
    def reverseMessage(self, message: str) -> str:
        # 第一步：去空格，列表
        c = message.split()
        print(c)
        # 第二步：倒序
        b = c[::-1]   # 从a索引开始走:走步 到第b索引（为负数就是倒数）（b【包括b】后面的不看）:（每步）一步长为c(形成等差数列）
        print(b)
        # 第三步 使用join
        a = ' '.join(b)
        return a

solution0 = Solution0
a = solution0.reverseMessage(solution0, "  qwe   123 abcd  ")
print(a)
'''作者：Candysad
链接：https://leetcode.cn/problems/fan-zhuan-dan-ci-shun-xu-lcof/solutions/2691982/jian-dan-ti-python-yi-xing-by-candysad-5yer/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。'''
