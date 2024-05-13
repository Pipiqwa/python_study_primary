try:
    user_height = float(input("输入身高"))
    user_weight = int(input("输入体重"))
    user_BMI = user_weight / user_height ** 2
except ValueError:
    print("输入不为合理数字")
except ZeroDivisionError:
    print("身高不能为0")
except:
    print("发生未知错误")
else:          # 没错误的话：
    print("BMI为：" + str(user_BMI))
finally:
    print("程序结束")
