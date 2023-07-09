# Python学习
# 学习时间：2022/9/25 18:09

# 获取当前的日期和时间
import datetime

curr_datetime = datetime.datetime.now()

print(curr_datetime, type(curr_datetime))

# 使用对象的方法将时间转换成为字符串类型
str_time = curr_datetime.strftime("%Y-%m-%d %H:%M:%S")
print("str_time", str_time)
# 同样也可以使用对象的方法，分别输出年，月，日
print("year:", curr_datetime.year)
print("month:", curr_datetime.month)
print("day:", curr_datetime.day)
print("hour:", curr_datetime.hour)
print("minute:", curr_datetime.minute)
print("second:", curr_datetime.second)

