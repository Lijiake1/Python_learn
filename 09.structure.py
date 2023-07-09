# Python学习
# 学习时间：2022/7/28 14:17
# money = 1000 # 余额
# s = int(input("请输入取款金额："))
## 判断余额是否充足
# if money >= s:
#     money -= s
#     print('取款成功，余额为：', money)

## 双分支结构
## 从键盘录入一个整数，编写程序，判断这个整数是奇数还是偶数

## 条件判断
# if num % 2 == 0:
#     print(num, '是偶数')
# else:
#     print(num, '是奇数')

# 多分支结构

num1 = int(input('请输入你的成绩：'))
if num1 >= 90 and num1 <= 100:
    print('A级')
elif num1 >= 80 and num1 < 90:
    print('B级')
elif num1 >= 70 and num1 < 80:
    print('C级')
elif num1 >= 60 and num1 < 70:
    print('D级')
elif num1 >= 0 and num1 < 60:
    print('E级')
else:
    print('不是有效的数据')

# python中特有的范围判断方法：
if 100 >= num1 >= 90:
    print('A级')
elif 90 > num1 >= 80:
    print('B级')
elif 80 > num1 >= 70:
    print('C级')
elif 70 > num1 >= 60:
    print('D级')
elif 60 > num1 >= 0:
    print('E级')
else:
    print('不是有效的数据')
