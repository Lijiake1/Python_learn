# Python学习
# 学习时间：2022/8/19 11:12

class Person(object):
    def __init__(self, name, age):
        print('__init__被调用了，self的id值为：{0}'.format(id(self)))
        self.name = name
        self.age = age

    def __new__(cls, *args, **kwargs):
        print('__new__被调用执行了，cls的id值为{0}'.format(id(cls)))
        obj = super().__new__(cls)
        print('创建的对象的id值为{0}'.format(id(obj)))
        return obj


print('object类对象的id值为：{0}'.format(id(object)))
print('Person类对象的id值为：{0}'.format(id(Person)))


p1 = Person('张三', 20)
print('p1这个Person类的实例化对象的id：{0}'.format(id(p1)))

