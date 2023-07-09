# Python学习
# 学习时间：2022/9/21 18:27
# 递归搜索出目录中最大的文件

import os
# 需要搜索的目录
search_dir = "E:\Graduate Courses"
# 存放每个文件的名称及大小的一个列表
result_files = []
# 使用os模块下的walk函数，walk会递归的遍历整个文件夹，并返回所有的目录以及文件
for root, dirs, files in os.walk(search_dir):
    for file in files:
        # 使用for循环将每一个文件的路径以及大小都存放在结果列表中
        file_path = f"{root}/{file}"
        result_files.append((file_path, os.path.getsize(file_path)/1000))
# 使用函数sorted函数将结果列表中的文件按照大小进行排列
print(sorted(
    result_files, key=lambda x : x[1], reverse=True
)[:10])
