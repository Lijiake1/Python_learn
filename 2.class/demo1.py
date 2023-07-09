# Python学习
# 学习时间：2022/8/18 9:04

from csv import reader
import numpy as np
filename = 'attachment3.csv'      # 这个文件中所有数据都是数字，并且数据中不包含文件头。
tu_array = []
with open(filename, 'rt') as raw_data:
    for line in raw_data:
        line = line[:-1]
        line = line.split(",")
        line = line[1:]
        tu_array.append(line)
print(tu_array)
for i in range(0, 607):
    print(len(tu_array[i]))

