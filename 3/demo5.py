# Python学习
# 学习时间：2022/8/18 16:10

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return '我的名字是{0}， 今年{1}岁了'.format(self.name, self.age)


stu = Student('张三', 20)
print(stu)


