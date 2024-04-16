"""
输入2，4，6
   3，7，9
输出2，3，4，6，7，9
"""
a = 0
list0 = []
input_str = input()
while input_str:
    a += 1
    input_list = input_str.split(',')

    # 记录输入
    for s in input_list:
        list0.append(int(s))
    # 第二次输入时
    if a == 2:
        # 排序
        sorted_list = sorted(list0)

        # 逐一转字符串
        str_output = ''
        for i in sorted_list:
            str_output += (str(i))
            # 加逗号
            str_output += ','

        # 输出
        print(str_output[:-1])

        a = 0
        list0 = []

    # 最后重新要求输入
    input_str = input()
