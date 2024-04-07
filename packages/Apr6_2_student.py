class Student:
    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id

    def introduce(self):
        print(f"Hello, my name is {self.name}, I am a student.")


"""
回调函数
"""
if __name__ == "__main__":
    def my_callback_function(arg):
        print(f"回调函数被调用，参数是: {arg}")


    # 定义一个函数，它接受一个回调函数作为参数
    def do_something_with_callback(callback, callBack):
        # 这里是一些操作...
        print("执行了一些操作...")
        # 然后调用回调函数，并传递一个参数

        callback("这是一个传递给回调函数的参数~~")


    # 使用上面定义的回调函数
    do_something_with_callback(my_callback_function, my_callback_function("a"))
    pass
