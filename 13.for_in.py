# Python学习
# 学习时间：2022/7/30 16:59

for item in 'Python':
    print(item)

# range() 产生的序列就是一个可迭代对象

for i in range(10):
    print(i)

# 如果循环中不需要使用到自定义变量，可以将自定义变量写为'_'

for _ in range(5):
    print('缘起性空')

print('使用for-in循环，计算1到100之间的偶数和')
sum = 0
for item in range(1, 101):
    if not bool(item % 2):
        sum += item

print('1到100之间的偶数和为', sum)


# 练习题：使用for-in循环显示100到999之间的水仙花数

'''for item in range(100, 1000):
    ge = item % 10
    shi = item // 10 % 10
    bai = item // 100
    print(bai, shi, ge)
    if ge ** 3 + shi ** 3 + bai ** 3 == item:
        print(item, '是水仙花数') '''


# 从键盘录入密码，最多录入三次，如果正确就结束循环

for item in range(3):
    pwd = input('请输入密码')
    if pwd == '8888':
        print('密码正确')
        break
    else:
        print('密码不正确')
