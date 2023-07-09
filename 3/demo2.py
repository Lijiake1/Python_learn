# Python学习
# 学习时间：2022/8/18 11:19

class Student:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def show(self):
        print(self.name, self.__age)


stu = Student('张三', 20)
stu.show()

print(stu.name)
# print(stu.age)

# 直接访问是不能访问的
# 但是可以使用别的方法访问

print(dir(stu))
print(stu._Student__age)
