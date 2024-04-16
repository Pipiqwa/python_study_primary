# 直接上堆栈  字符串拼接 直接操作字符串
# 代码量少 但是 占用内存更多

str_input = input()
while str_input:

    # 记录单个单词
    str_charactor = ""
    # 将字符单词记录列表
    str_charactor_line = ""
    # 一旦出现空格 跳过  但是要在空格再次出现时，其单词记录时连续的
    for s in str_input:
        # 如果出现空格
        if s == ' ':
            # 单词记录不为空的话
            if str_charactor != "":
                # 添加记录到单词 句子
                str_charactor_line = (" " + str_charactor) + str_charactor_line
                # 清空单词记录容器
                str_charactor = ""
            # 为空 无事发生
        # 出现字符的话
        else:
            # 记录单词
            str_charactor += s
    # 最后一次不为空的话，补上最后一次记录的单词 str_charactor
    if str_charactor != "":
        str_charactor_line = (" " + str_charactor) + str_charactor_line

    print(str_charactor_line[1:])
    str_input = input()
