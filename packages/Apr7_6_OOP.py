# Object Oriented Programming

class Student:  # Pascal命名法
    def __init__(self, name, num1, num2):  # 特殊方法 定义函数   定义实例对象的属性  （第一个参数永远被self占用）
        self.name = name
        self.student_id = num1
        self.grade_year = num2
        self.grades = {"语文": 0, "数学": 0, "英语": 0}

    def speak(self):
        print(f"你好，我叫{self.name},学号是{self.student_id},现在是{self.grade_year}年级")

    def set_grades(self, course, grade):
        if course in self.grades:
            self.grades[course] = grade

    def print_grades(self):
        for course in self.grades:
            print(f"{course}:{self.grades[course]}")


student1 = Student("小明", 113, 3)
print("学生名字叫{0}，学号是{1}，年级是{2}".format(student1.name, student1.student_id, student1.grade_year))
student1.speak()
student1.set_grades("数学", 99)
student1.print_grades()

def is_has_or_not(has_little_bag):
    if has_little_bag:
        return "有"
    else:
        return "没有"

class pupil(Student):
    def __init__(self, name, student_id, grade_year, bool_has_bag):
        super().__init__(name, student_id, grade_year)
        self.has_little_bag = bool_has_bag

    def do_homework(self):  # 方法
        print("写小学作业")

    def pupil_speak(self):
        print(f"你好，我叫{self.name},学号是{self.student_id},现在是{self.grade_year}年级，{is_has_or_not(self.has_little_bag)}一个书包")




pupil1 = pupil("小小", 113, 1, True)
pupil1.pupil_speak()


class undergraduate(Student):
    def do_homework(self):
        print("写大学作业")


