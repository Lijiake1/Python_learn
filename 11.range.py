# Python学习
# 学习时间：2022/7/30 8:48

# 第一种创建方式，只有一个参数
r = range(10) # 默认从0开始，默认的间隔是1
print(r)
print(list(r)) # 使用列表来查看迭代器中存储的对象

# 第二种创建方式，有两个参数
r = range(1, 10) # 指定了起始值，从1开始
print(list(r)) #

# 第三种创建方式，有三个参数
r = range(1, 20, 2)
print(list(r))

# 判断指定的整数，是否在序列中存在 in, not in
print(10 in r)
print(10 not in r)
