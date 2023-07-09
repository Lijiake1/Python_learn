# Python学习
# 学习时间：2022/9/14 18:33
# 按照文件后缀整理文件

import os
import shutil
dir = "./arrange_dir"
# 通过os模块下的listdir函数，将目录中的文件名转化为列表，并使用for循环依次访问
for file in os.listdir(dir):
    # 通过os模块下的splitext函数将文件的后缀名保存在变量ext中
    ext = os.path.splitext(file)[1]
    # 将ext中后缀名的.去掉
    ext = ext[1:]
    # 通过os模块中的isdir函数判断文件夹中是否有名为ext的文件夹
    if not os.path.isdir(f"{dir}/{ext}"):
        # 如果没有的话就新建一个
        os.mkdir(f"{dir}/{ext}")
    # 在变量中存储文件的源文件夹
    srouce_path = f"{dir}/{file}"
    # 在变量中存储文件的移动目标文件夹
    target_path = f"{dir}/{ext}/{file}"
    # 使用shutil模块中的move函数将文件进行移动
    shutil.move(srouce_path, target_path)
    print(file)
