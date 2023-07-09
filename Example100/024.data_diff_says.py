# Python学习
# 学习时间：2022/9/26 20:07
# 计算任意七天前的日期

import datetime


def get_diff_days(pdate, days):
    # 将字符串日期转换成为一个datetime.datetime对象
    pdate_obj = datetime.datetime.strptime(pdate, "%Y-%m-%d")
    # 将时间间隔days转换成为一个时间间隔对象
    time_gap = datetime.timedelta(days=days)
    # 通过将pdate_obj对象减去间隔从而得到想要的结果
    pdate_result = pdate_obj - time_gap
    # 将日起对象里面保存的内容输出为年月日对象
    return pdate_result.strftime("%Y-%m-%d")


print(get_diff_days("2022-09-26", 1))
