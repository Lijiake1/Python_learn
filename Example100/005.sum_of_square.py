# Python学习
# 学习时间：2022/9/8 21:40

# 给定一个数字，计算从0到这个数字的所有数字之和

def sum_of_square(n):
    result = 0
    for number in range(1, n + 1):
        result += number * number
    return result



print('sum of square 3:', sum_of_square(3))
print('sum of square 5:', sum_of_square(5))
print('sum of square 10:', sum_of_square(10))

