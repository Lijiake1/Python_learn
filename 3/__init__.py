# Python学习
# 学习时间：2022/8/18 11:15
# number_array = []
# with open("./data_number,txt", encoding="utf-8") as fin:
#     for line in fin:
#         line = line[:-1]
#         print(line, type(line))
#         if (line.isdigit()):
#
#
#             line = int(line)
#             number_array.append(line)
# print(number_array)
# flag = False
# for i in range(0, 607):
#     for item in number_array:
#         if (i == item):
#             flag = True
#     if (flag):
#         flag = False
#     else:
#         print(i)
number_array = []
with open("./data.txt", encoding="utf-8") as fin:
    for line in fin:
        if line.isspace():
            pass
        else:
            line = int(line[:-1])
            number_array.append(line)
flag = False
now_array = []
with open("./data_number,txt", encoding="utf-8") as fin:
    for line in fin:
        line = int(line[:-1])
        now_array.append(line)
for i in now_array:
    for item in number_array:
        if (i == item):
            flag = True
    if (flag):
        flag = False
    else:
        print(i)
