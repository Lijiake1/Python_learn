# Python学习
# 学习时间：2022/9/25 18:36

import datetime
birthday = "1999-12-16"
birthday_date = datetime.datetime.strptime(birthday, "%Y-%m-%d")

curr_datetime = datetime.datetime.now()
print(curr_datetime, type(curr_datetime))

distance_of_datetime = curr_datetime - birthday_date
print(distance_of_datetime, type(distance_of_datetime))
print(distance_of_datetime.days)
