# Python学习
# 学习时间：2022/10/1 13:57
# 批量获取网页中的手机号码
import re

pattern = r"1[3-9]\d{9}"
file_cont = ""
with open("./input_data/webpage_pthone_numbers.txt", encoding="utf-8") as fin:
    file_cont = fin.read()
results = re.findall(pattern, file_cont)
print(len(results))
for item in results:
    print(item)
