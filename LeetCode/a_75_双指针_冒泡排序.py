"""
75. 颜色分类
中等
相关标签  数组  双指针  排序
提示
给定一个包含红色、白色和蓝色、共 n 个元素的数组 nums ，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

必须在不使用库内置的 sort 函数的情况下解决这个问题。

输入：nums = [2,0,2,1,1,0]
输出：[0,0,1,1,2,2]

输入：nums = [2,0,1]
输出：[0,1,2]

"""

while True:
    a = input()
    b = a[8:-1]
    c = b.split(",")

    left = 0
    right = len(c)
    have_exchanged_times = 0
    can_break_while = False

    while True:
        have_exchanged_times = 0
        for i in range(0, right):   # 使用冒泡排序
            if i != right - 1:
                if c[i] > c[i + 1]:

                    c[i],c[i + 1] = c[i+1],c[i]

                    have_exchanged_times += 1
            elif have_exchanged_times == 0:
                can_break_while = True
                print(f"[{",".join(c)}]")
                print(list(map(int,c)))
                break
        if can_break_while:
            break
