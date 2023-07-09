# Python学习
# 学习时间：2022/9/30 14:24
# 将Unix时间戳转换为北京时间

import datetime
unix_time = 1664519272
datetime_objt = datetime.datetime.fromtimestamp(unix_time)
datetime_str = datetime_objt.strftime("%Y-%m-%d %H:%M:%S")
print(datetime_str)
