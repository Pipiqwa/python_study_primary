class Solution:
    def sortColors(self, nums: list[int]):
        for i in range(len(nums)-1):
            for j in range(len(nums)-i-1):
                if nums[j]>nums[j+1]:
                    nums[j],nums[j+1]=nums[j+1],nums[j]
        return nums

a = Solution
b = [5,4,3,2,1]
c = a.sortColors(a,b)
print(c)
"""
作者：我是菜鸡-0xff

最基础的冒泡排序，虽然时间效率低，但好写

链接：https://leetcode.cn/problems/sort-colors/solutions/2145974/zui-ji-chu-de-mou-pao-pai-xu-sui-ran-shi-j0k8/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""
