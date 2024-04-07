total: int = 0
for i in range(1, 101, 2):
    total = total + i
print(total)
print("\n")

# 列表
temperature_list = [36, 37, 38, 35, 35.6, 37.7, ]
print(temperature_list[1])
print(len(temperature_list))
print(temperature_list)

for temperature in temperature_list:
    if temperature >= 37:
        print("玩球了")
print("\n")

# 字典
temperature_dictionary = {'张三': 36.4, '李四': 37, '王五': 37.5}
print(temperature_dictionary.keys())
print(temperature_dictionary.values())
print(temperature_dictionary.items())  # 化为tuple 元组
# 2种写法
for staff_id,temperature in temperature_dictionary.items():  # for temperature_tuple in temperature_dictionary;
    if temperature >= 37:                                    # staff_id = temperature_tuple[0]
        print(staff_id+" "+str(temperature))                 # temperature = temperature_tuple[2]
print("\n")

# 字符串
original_str = "123"
# 使用列表推导式将每个字符转换为整数，加1，然后转换回字符串
result_str = ''.join(str(int(char) + 1) for char in original_str)

for char in result_str:
    result_str += ''.join(str(int(char) + 1))

print(result_str)
