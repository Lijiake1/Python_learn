# Python学习
# 学习时间：2022/7/30 10:13

# 用while循环计算1到100之间的偶数和

sum = 0
a = 1
while a <= 100:
    if not bool(a % 2):
        sum += a

    a += 1

print('1到100之间的偶数和为', sum)
