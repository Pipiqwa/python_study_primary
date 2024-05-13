left = 2
l_ = 'ww'
left = 0 if not isinstance(l_, (int, float)) else l_

print(left)
print('abc' if left == 2 else '2233333')

a = (1 == 1)
b = (2 == 2)
if any([a, b]):
    pass


squares = [x**2 for x in range(10)]  # 创建一个包含0到9的平方的列表

square = [x**2,lambda y:y+1]  # 创建一个包含0到9的平方的列表

y = lambda x:x+1
y(1)
print(squares)

a = [i for i in squares]