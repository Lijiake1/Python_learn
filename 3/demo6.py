# Python学习
# 学习时间：2022/8/19 10:02

class Animal(object):
    pass


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age



class Student(Animal, Person):
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


stu1 = Student('张三', 20)
print(stu1.__dict__)
print(Student.__dict__)
print(stu1.__class__)
print(Student.__bases__) # 查看类所继承的类
print(Student.__base__) # 查看类继承的第一个类
print(Student.__mro__) # 查看类的内部结构
print(Person.__subclasses__()) # 显示子类的列表
