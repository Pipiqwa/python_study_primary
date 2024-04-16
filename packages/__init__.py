# 导入包中的一些模块，使得它们可以直接通过包名访问   记得在脚本名前加 .
from .Apr6_2_student import Student

# 可以添加一些简单的逻辑，比如打印欢迎信息
def __getattr__(name):
    print(f"Welcome to the student_management package. You tried to access {name} which is not defined.")