# Python学习
# 学习时间：2022/9/8 22:09

def get_unique_list(lista):
    result = []
    for item in lista:
        if item not in result:
            result.append(item)
    return result


lista = [10, 20, 30, 10, 20]
print(f'srouce list {lista}, unique list:', get_unique_list(lista))
print(f'srouce list {lista}, unique list:', list(set(lista)))
