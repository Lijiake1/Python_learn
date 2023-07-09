# Python学习
# 学习时间：2022/8/25 18:11

import numpy as np

# w, v = np.linalg.eig(np.array([[1, 1/2, 4, 3, 3],
#                                [2, 1, 7, 5, 5],
#                                [1/4, 1/7, 1, 1/2, 1/3],
#                                [1/3, 1/5, 2, 1, 1],
#                                [1/3, 1/5, 3, 1, 1]]))
# a = input('')
# w, v = np.linalg.eig(np.array([[2, 2, -2], [2, 5, -4], [-2, -4, 5]]))
# print('{0}'.format(w))
# print('-------------------------')
# print('{0}'.format(v))

num = input()
sum = 0
dict1 = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
i = -1
length = len(num)
while(abs(i) <= length):
    g = num[i] # 保存每一位的数字
    if g.isdecimal():
        sum = sum + (int(g) * (16 ** (abs(i) - 1)))
    else:
        sum = sum + (int(dict1[g]) * (16 ** (abs(i) - 1)))
    i -= 1
print(sum)
