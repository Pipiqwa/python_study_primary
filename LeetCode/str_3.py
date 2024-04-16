# 输入一串字符，输出字符串中出现次数最多的字符的数量

charactor_count_dict = {}  # 建立字典charactor_count_dict key 为字符  value 为 字符出现次数  int
str_input = input()  # 记录输入  str_input
while str_input:
    # for循环， for str in str_input
    for str0 in str_input:
        if str0 in charactor_count_dict:   # any_dict.keys()是列出字典所有的key
            charactor_count_dict[str0] += 1
        else:
            charactor_count_dict[str0] = 1

    max_count = 0
    max_count_charactor = ''
    # 判断最大字符
    for str_charactor,count in charactor_count_dict.items():
        if max_count < count:
            max_count = count
            max_count_charactor = str_charactor

    print(f"{max_count},{max_count_charactor}")
    print(f"所有key：{charactor_count_dict.keys()}")
    charactor_count_dict = {}
    str_input = input()