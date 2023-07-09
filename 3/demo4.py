# Python学习
# 学习时间：2022/8/18 11:34

class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def info(self):
        print(self.name, self.age)

class Student(Person):
    def __init__(self, name, age, stu_num):
        super().__init__(name, age)
        self.stu_num = stu_num
    def info(self):
        super().info()
        print(self.stu_num)

class Teacher(Person):
    def __init__(self, name, age, teachofyear):
        super().__init__(name, age)
        self.teachofyear = teachofyear

    def info(self):
        super().info()
        print(self.teachofyear)

stu = Student('张三', 20, '1001')
teacher = Teacher('李四', 34, 10)


stu.info()
teacher.info()
