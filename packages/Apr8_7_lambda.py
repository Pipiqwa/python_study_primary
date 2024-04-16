# 匿名函数 Lambda
"""
一般要有被传入的东西
"""

(lambda:None)()
print((lambda:None)())


print((lambda x:1+x)(2))

print((lambda x,y:1+x+y)(2,3))