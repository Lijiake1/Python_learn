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


# 类属性的使用方式
print(Student.native_pace)
stu1 = Student('张三', 20)
stu2 = Student('李四', 30)
print(stu1.native_pace)
print(stu2.native_pace)
Student.native_pace = '天津'
print(stu1.native_pace)
print(stu2.native_pace)


Student.cm()
Student.method()
