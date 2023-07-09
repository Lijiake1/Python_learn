# Python学习
# 学习时间：2022/9/25 21:09

name_list = []
i = 1
new_list = []
with open("name_data.txt", encoding="utf-8") as fin:
    for line in fin:
        if line.isspace():
            pass
        else:
            name_list.append(line)
print(name_list)

with open("star_name.txt", "w", encoding="utf-8") as fin:
    for line in name_list:
        line = line[:-1]
        fin.write(line)
        fin.write('\n')
