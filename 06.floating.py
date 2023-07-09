# Python学习
# 学习时间：2022/7/21 12:32

# 浮点数存储的时候会有一定的误差，可以使用python包decimal进行精确

from decimal import Decimal

print(Decimal('1.1') + Decimal('2.2'))
str1 = 'abc'
print(str1)
str1 = 'acd'

print(str1)
name = '张三'
age = 20
print("我的名字是" + name)
print("我的年龄是" + str(age))
