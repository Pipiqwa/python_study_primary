import statistics
print(statistics.median([1,2,35,8,25]))

from statistics import median
print(median([1,2,35,8,25]))

from statistics import *  # all 增加命名冲突风险
print(median([1,2,35,8,25]))

# 引入第三方库（pypi.org） 可以在终端 pip install 库名字