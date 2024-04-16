gpa_dict = {'张三': 3.4545, '李四': 3.5532, '王五': 2.3456432}

for name, gpa in gpa_dict.items():
    print(f"""{name}你好，
    你的绩点为：{gpa:.2f}""")  # {0}被第一个参数替换

print("\n")
for name, gpa in gpa_dict.items():
        print("{0}你好，你的绩点为：{1:.3f}".format(name, gpa))  # {0}被第一个参数替换