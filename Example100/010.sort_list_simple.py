# Python学习
# 学习时间：2022/9/8 22:18

lista = [20, 30, 40, 50, 10]
# 使用方法对原列表进行排序
lista.sort()
# 使用函数对列表排序，并将排序后的结果保存在另一个列表中
# 可用通过参数控制升序和降序
listb = sorted(lista, reverse=True)
print(f'lista is {lista}')
print(f'listb is {listb}')
