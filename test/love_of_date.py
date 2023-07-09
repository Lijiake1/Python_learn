# Python学习
# 学习时间：2022/9/25 18:47
from turtle import *
"""
import datetime
man_name = input("请输入你的名字：")
woman_name = input("请输入那个可爱公主的名字：")
time_begin = input("请输入你们在一起的时间（输入格式：1999-1-1）：")
datetime_begin = datetime.datetime.strptime(time_begin, "%Y-%m-%d")
curr_datetime = datetime.datetime.now()
distance_date = curr_datetime - datetime_begin
distance_stringdate = str(distance_date.days)
print(f"哇，今天是{man_name}和美丽的{woman_name}公主在一起的第{distance_stringdate}天")
"""

def curvemove():
    for i in range(200):
        right(1)
        forward(1)


color('red','pink')
begin_fill()
left(140)
forward(111.65)
curvemove()
left(120)
curvemove()
forward(111.65)
end_fill()
done()
