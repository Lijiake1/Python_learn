# Python学习
# 学习时间：2022/9/8 17:44
import math

# 使用math库中的函数计算公式

def compute_area_of_circle(r):
    return round(math.pi * r * r, 2)


print('area of 2 is:', compute_area_of_circle(2))
print('area of 3.14 is:', compute_area_of_circle(3.14))
print('area of 6.78 is:', compute_area_of_circle(6.78))
