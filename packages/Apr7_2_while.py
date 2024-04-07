# 简单 观察者模式
class InputHandler:
    def __init__(self):
        self.on_input_b = None  # 用于绑定当输入为 'b' 时的回调函数

    def set_on_input_b(self, callback):
        self.on_input_b = callback  # 设置回调函数

    def handle_input(self, input_value):
        if input_value == 'b':
            self.on_input_b()  # 调用回调函数
        else:
            # 处理其他输入...
            print(f"处理其他输入: {input_value}")


def on_input_b():
    print("输入为 'b'，继续下一次循环。")
    return True  # 返回 True 表示已经处理了 'b' 输入


input_handler = InputHandler()
input_handler.set_on_input_b(on_input_b)

# 模拟循环处理输入
for _ in range(5):
    user_input = input("请输入（输入 'b' 继续循环）：")
    input_handler.handle_input(user_input)
