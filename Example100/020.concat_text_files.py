# Python学习
# 学习时间：2022/9/22 13:59
# 将一个文件夹中的多个文件合并成一个文件
import os

# 将需要读取的文件夹目录存在一个变量中
data_dir = "./input_data/many_texts"
contents = []
# 使用for循环以及os模块的listdir函数将文件夹中的文件名依次读取
for file in os.listdir(data_dir):
    # 提取出每一个文件的路径
    file_path = f"{data_dir}/{file}"
    # 判断文件是否是我们需要的txt文件
    if os.path.isfile(file_path) and file.endswith(".txt"):
        # 如果是我们需要的文件，那么将文件中的内容依次放在列表中
        with open(file_path, encoding="utf-8") as fin:
            contents.append(fin.read())
# 将读取到的文件使用换行符连接起来放在一个字符串变量中
final_content = "\n".join(contents)

# 新建一个文件将合并后的文件内容存起来
with open("./output_data/many_texts.txt", "w", encoding="utf-8") as fin:
    fin.write(final_content)
