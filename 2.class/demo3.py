# Python学习
# 学习时间：2022/8/18 9:07

class Student:
    native_pace = '吉林' # 直接写在类里面的变量称为类属性

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 实例方法
    def eat(self):
        print('学生在吃饭....')

    # 静态方法
    @staticmethod
    def method():
        print('我使用了staticmethod')
    # 类方法
    @classmethod
    def cm(cls):
        print('这是一个类方法')


# 实例化对象
stu1 = Student('张三', 19)
# stu1.eat()
# print(stu1.name)
# print(stu1.age)
print(stu1.__dict__)
print(Student.__dict__)

# 另一种调用对象方法的方法

# Student.eat(stu1)
