"""
坐标移动
输入：
A10;S20;W10;D30;X;A1A;B10A11;;A10;
输出：
10,-10
"""
a = input()
b = a.split(";")
x = 0
y = 0

index_error, value_error, other_error = 0, 0, 0

for i in b:
    try:
        if i[0] == 'A':
            x -= int(i[1:])
        elif i[0] == 'D':
            x += int(i[1:])
        elif i[0] == 'S':
            y -= int(i[1:])
        elif i[0] == 'W':
            y += int(i[1:])
    except IndexError:
        index_error += 1
    except ValueError:
        value_error += 1
    except:
        other_error += 1
    else:    # 没有任何错误的话 走这里 然后走下面
        continue
    finally:   # 有错误 会走这里
        continue

print(x, y)
print(f"索引错误：{index_error}，值错误：{value_error}，其他错误：{other_error}")
