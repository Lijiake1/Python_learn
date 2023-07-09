# Python学习
# 学习时间：2022/9/30 14:47
# 计算日期数据周同比

import datetime

date_sale = {}
is_first_line = True
with open("./input_data/date_sale_data.txt", encoding="utf-8") as fin:
    for line in fin:
        if is_first_line:
            is_first_line = False
            continue
        line = line[:-1]
        date, sale_number = line.split("\t")
        date_sale[date] = float(sale_number)


def get_diff_days(date, days):
    curr_date = datetime.datetime.strptime(date, "%Y-%m-%d")
    timedlta = datetime.timedelta(days=-days)
    return (curr_date + timedlta).strftime("%Y-%m-%d")


for date, sale_number in date_sale.items():
    date7 = get_diff_days(date, 7)
    sale_number7 = date_sale.get(date7, 0)
    if sale_number7 == 0:
        print(date, sale_number, 0)
    else:
        week_diff = (sale_number - sale_number7) / sale_number
        print(date, sale_number, date7, sale_number7, week_diff)

