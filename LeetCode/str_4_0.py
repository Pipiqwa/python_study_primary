# 字符串中的单词反转
"""
LCR 181. 字符串中的单词反转

示例 1：
输入: message = "the sky is blue"
输出: "blue is sky the"
示例 2：
输入: message = "  hello world!  "
输出: "world! hello"
解释: 输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
示例 3：
输入: message = "a good   example"
输出: "example good a"
解释: 如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。
"""

str_input = input()
while str_input:
    # 记录单个单词
    str_charactor = ""
    # 将字符单词记录列表
    str_charactor_list = []
    # 一旦出现空格 跳过  但是要在空格再次出现时，其单词记录时连续的
    for s in str_input:
        # 如果出现空格
        if s == ' ':
            # 单词记录不为空的话
            if str_charactor != "":
                # 添加记录到单词表
                str_charactor_list.append(str_charactor)
                # 清空单词记录容器
                str_charactor = ""
            # 为空 无事发生
        # 出现字符的话
        else:
            # 记录单词
            str_charactor += s
    # 最后一次不为空的话，补上最后一次记录的单词 str_charactor
    if str_charactor != "":
        str_charactor_list.append(str_charactor)

    print(str_charactor_list)

    # 列表反转 str_charactor_list
    new_charactor_list = []
    length_list = len(str_charactor_list)
    for i in range(0,length_list):  # in range [1,10) 会不包括10
        new_charactor_list.append(str_charactor_list[length_list-1-i])

    # 逐一打印 成一句字符串
    # new_charactor_list.append(str_charactor_list[length_list-1])  # += 是会逐一加上 str 的一个一个的字符 列为表
    print(new_charactor_list)
    new_line = ""
    for char in new_charactor_list:
        new_line += (char+" ")
    print(new_line[:-1])

    # 重新建立输入
    str_input = input()
