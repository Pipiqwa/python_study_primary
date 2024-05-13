import os

# 指定要重命名的文件夹路径
folder_path = '../HJ_牛客'

# 重命名函数，可以根据需要修改函数体来实现不同的重命名规则
def rename_files(directory):
    for filename in os.listdir(directory):
        # 构造新的文件名，这里只是简单地在原文件名前添加了前缀'new_'


        if filename[2] != '_':
            new_filename = filename[:2] + '_' + filename[2:]

            # 构造完整的文件路径
            old_file = os.path.join(directory, filename)
            new_file = os.path.join(directory, new_filename)
            # 重命名文件
            os.rename(old_file, new_file)
            print(f'Renamed "{filename}" to "{new_filename}"')


# 调用函数进行重命名
rename_files(folder_path)