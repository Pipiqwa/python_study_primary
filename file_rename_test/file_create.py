import os

# 假设我们想要在当前目录下的 'my_files' 子目录中创建文件
directory = '../HJ_niuke'

# 确保目录存在
if not os.path.exists(directory):
    os.makedirs(directory)

for i in range(1, 108):
    filename = f'hj_{i}.py'
    # 使用os.path.join()来构建完整的文件路径
    full_path = os.path.join(directory, filename)

    # 构造相对路径文件名
    relative_path = f'{directory}/hj_{i}.py'
    # 确保路径分隔符是正斜杠，以提高跨平台兼容性
    # relative_path.replace('\\', '/')

    with open(relative_path, 'w') as file:
        file.write(f'# This is file {filename}'
                   '\n\"\"\"'
                   '\n'
                   '\n"""')
    print(f'Created file: {relative_path}')
