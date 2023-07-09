# Python学习
# 学习时间：2022/7/29 13:05
num_a = int(input('请输入第一个整数：'))
num_b = int(input('请输入第二个整数：'))

print('使用条件表达式进行比较')
print(str(num_a) + '大于等于' + str(num_b) if num_a >= num_b else str(num_a) + '小于' + str(num_b))
