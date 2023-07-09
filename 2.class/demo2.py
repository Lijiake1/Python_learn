# Python学习
# 学习时间：2022/8/18 9:07
import re
# dict1 = {}
# with open("./usepython.txt", encoding="utf-8") as fin:
#     for line in fin:
#         line = line[:-1]
#         key, value = line.split(":")
#         # print(key, value)
#         if key not in dict1:
#             dict1[key] = value
# list_number = []
# for key, value in dict1.items():
#     if value == " 1.0":
#         list_number.append(key)
# print(list_number)


with open("./right_number.txt", encoding="utf-8") as fin:
    for line in fin:
        line = line[:-1]
        waste, block, assembly = line.split("_")
        if assembly == '26':
            print(block, end='、')

# for key, value in dict1.items():
#     if value == ' 1.0':
#         if(re.match("x_\d{2}_1", key)):
#             print(key[2:4])
#         elif(re.match("x_\d{1}_1", key)):
#             print(key[2:3])
#         elif(re.match("x_\d{3}_1", key)):
#             print(key[2:5])



