# Python学习
# 学习时间：2022/9/8 21:51

# 给定一个范围，输出这个范围中所有的偶数


def get_even_numbers(begin, end):
    result = []
    for item in range(begin, end):
        if item % 2 == 0:
            result.append(item)
    return result
begin = 4
end = 15

data = [item for item in range(begin, end) if item % 2 == 0]
print(f'begin = {begin}, end = {end}, even numbers:', get_even_numbers(begin, end))
print(f'begin = {begin}, end = {end}, even numbers:', data)
