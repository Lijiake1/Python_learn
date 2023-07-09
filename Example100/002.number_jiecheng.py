# Python学习
# 学习时间：2022/9/8 17:13

# 定义一个函数计算参数的阶乘
def get_jiecheng(number):
    result = 1
    while number > 0:
        result *= number
        number -= 1
    return result


print('阶乘6 = ', get_jiecheng(6))
print('阶乘3 = ', get_jiecheng(3))
print('阶乘100 = ', get_jiecheng(100))
