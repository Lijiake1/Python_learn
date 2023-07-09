# Python学习
# 学习时间：2022/8/21 9:35

import os
path = os.getcwd()
print(path)
lst_files = os.walk(path)
for dirpath, dirname, filename in lst_files:
    print(dirpath)
    print(dirname)
    print(filename)
