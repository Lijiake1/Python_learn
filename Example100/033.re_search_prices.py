# Python学习
# 学习时间：2022/10/12 20:28

contents = """
小明上街买菜
买了1斤黄瓜花了8元；
买了2斤葡萄花了13.5元；
买了3斤白菜花了5.4元；
"""
# 要求提取（1、黄瓜、8）、（2、葡萄、13.5）、（3、白菜、5.4）
import re

for line in contents.split("\n"):
    pattern = r"(\d)斤(.*)花了(\d+(\.\d+)?)元"
    """ pattern解析：'\d斤'：\d表示一个数字，后面跟着的是斤字
    .*表示这里有若干个字符, \d还是表示数字
    (\.\d+)?: '\.'表示是小数点的转义字符，'\d'表示数字， '？'表示可能会有一个小数点加上数字
    """
    # 使用re.search函数可以将正则表达式与字符串进行匹配，如果匹配成功，将会返回一个match对象
    # match对象就是一次匹配的结果，包含了很多匹配的相关信息
    # 通过match.group(i)将match对象中的分组信息提取出来，i就是第i个分组
    match = re.search(pattern, line)
    if match:
        print(f"{match.group(1)}\t{match.group(2)}\t{match.group(3)}")
