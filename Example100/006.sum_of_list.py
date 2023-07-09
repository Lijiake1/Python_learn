# Python学习
# 学习时间：2022/9/8 21:45

# 给定一个列表，计算这个列表中的所有数字之和

def sum_of_list(param_list):
    total = 0
    for number in param_list:
        total += number
    return total


list1 = [1, 2, 3, 4]
list2 = [17, 5, 3, 5]

print(f'sum of {list1} :', sum_of_list(list1))
print(f'sum of {list2} :', sum_of_list(list2))

print(f'sum of {list1} :', sum(list1))
print(f'sum of {list2} :', sum(list2))
