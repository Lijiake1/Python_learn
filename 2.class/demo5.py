# Python学习
# 学习时间：2022/8/18 9:07

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def eat(self):
        print(self.name + '在吃饭')


stu1 = Student('张三', 20)
stu2 = Student('李四', 30)

# 动态的给予stu1添加属性‘性别’

stu1.gender = ('女')
print(stu1)
print(dir(Student))

# 动态的给stu1绑定方法show()


def show():
    print('这是一个函数')


stu1.show = show

