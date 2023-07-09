# Python学习
# 学习时间：2022/9/30 14:09
# 计算两个日期之间的所有日期
import datetime


def get_date_range(begin_date, end_date):
    date_list = []
    while begin_date <= end_date:
        # 从起始日期开始将每一天都加入日期列表中
        date_list.append(begin_date)
        # 将字符串内的日期转换成为一个日期对象
        begin_date_object = datetime.datetime.strptime(begin_date, "%Y-%m-%d")
        # 设置一个日期间隔为1
        days1_timedelta = datetime.timedelta(days=1)
        # 将起始日期加上这个日期间隔，并格式化为年月日的形式重新赋给其实日期
        begin_date = (begin_date_object + days1_timedelta).strftime("%Y-%m-%d")
    return date_list

begin_date = "2021-04-28"
end_date = "2021-05-03"
date_list = get_date_range(begin_date, end_date)
print(date_list)



