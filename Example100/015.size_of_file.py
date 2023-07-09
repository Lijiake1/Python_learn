# Python学习
# 学习时间：2022/9/14 15:24
# 统计一个目录下文件的大小

import os

# 使用os模块的getsize函数获得一个文件的大小
print(os.path.getsize("./input_data/Beginner Guide to Python.txt"))
# 初始化一个变量存放文件大小
sum_size = 0
# 使用for循环遍历目录中的每一个文件
for file in os.listdir("."):
    if os.path.isfile(file):
        print(file)
        # 在总文件大小变量中加上此次遍历的文件的大小
        sum_size += os.path.getsize(file)

# 输出文件夹中的文件总大小
print("the size of all file in Example100 is:", sum_size/1000)
