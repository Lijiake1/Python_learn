# Python学习
# 学习时间：2022/10/1 13:39
# Python从文本中提取手机号码
import re
contents = """
        白日依19989881888山尽，黄河入45645546468798978海流
        欲穷12345千里目，更上15619292345一层楼
"""

pattern = r"1[3-9]\d{9}"

results = re.findall(pattern, contents)
for item in results:
    print(item)
