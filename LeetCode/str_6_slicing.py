def rotate(input, d):
    Lfirst = input[0: d]
    Lsecond = input[::]      # 从x索引开始走:步到第x索引（为负数就是倒数）（x【包括x】后面的不看）:（每步）一步长(形成等差数列）
    Rfirst = input[0: len(input) - d]
    Rsecond = input[len(input) - d:]

    print("头部切片翻转 : ", (Lsecond + Lfirst))
    print("尾部切片翻转 : ", (Rsecond + Rfirst))


if __name__ == "__main__":
    input = 'cba012345689'
    d = 2  # 截取两个字符
    rotate(input, d)
