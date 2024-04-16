# 学习 str_4_2 的思路
str_input = input()
while str_input:
    # 第一步：去空格，列表
    str_charactor_list = str_input.split()
    new_charactor_list = []
    l = len(str_charactor_list)
    # 第二步：倒序
    for i in range(0,l):
        new_charactor_list.append(str_charactor_list[l-1-i])  # 注意列表添加 使用append 不要使用+=
    # 第三步 使用join
    new_line = ' '.join(new_charactor_list)
    print(new_line)
    str_input = input()