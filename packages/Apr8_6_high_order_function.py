def calculate_and_print(calculator,num, num_):
    result = calculator(num,num_)
    print(f"""
    | 数字参数 | {num} |
    | 计算结果 | {result} |
    """)


def calculate_square(num,num_):
    return num * num


def calculate_cube(num):
    return num * num * num


def calculate_plus(num1, num2):
    return num1 + num2


calculate_and_print(calculate_square,2,None)
