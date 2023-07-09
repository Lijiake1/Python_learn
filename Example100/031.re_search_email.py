# Python学习
# 学习时间：2022/10/1 14:12
# 自动提取邮箱地址
import re
contents = """
        寻隐者12345@qq.com不遇
        朝代：唐asdf12dsa#abc.com代
        作python666@163.com者：贾岛
        松下问童子，言师python-abc@163com采药去。
        只在python_ant-666@sine.net此山中，云深不知处。
"""

pattern = re.compile(r"""
    [a-zA-Z0-9_-] + 
    @
    [a-zA-Z0-9] +
    \.
    [a-zA-Z]{2,4}
""", re.VERBOSE)
results = pattern.findall(contents)

for item in results:
    print(item)
