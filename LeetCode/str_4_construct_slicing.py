def sorting(str_input):  # 构建slice用法[ 从a索引开始走:走步 到第b索引（为负数就是倒数）（b【包括b】后面的不看）:（每步）一步长为c(形成等差数列）]
    a = 0
    b = len(str_input) - 1
    c = 1
    left = a
    right = b

    str_char = ''   # 单词容器
    str_output = ''    # 输出

    while left <= right:  # 从右往左（反向）
        if str_input[right] != ' ':          # 遍历不为空格
            str_char = str_input[right] + str_char      # 23  2+3  3是先得到的
            right -= 1
        else:                                # 出现空格
            if str_char == '':
                right -= 1
            else:
                str_output += str_char + ' '
                str_char = ''
                right -= 1

    if str_char != '':    # 最后判断 单词容器是否为空
        str_output += str_char + ' '
    return str_output


a = sorting("   012  345    76876 ")

x = 0
y = len(a) - 1  # 忽略最后一位
b = ''
for s in a:
    if x < y:
        b += a[x]
        x += 1

print(b)
print(a[:-1])