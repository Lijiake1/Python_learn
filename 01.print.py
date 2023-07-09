# Python学习
# 学习时间：2022/7/21 12:16

#print可以输出数字
print(520)
print('helloword')

#可以输出字符串
print('helloworld')

#可以输出含有运算符的表达式
print(3+1)

#将数据输出到文件
fp = open('F:/test.txt', 'a+') #权限a+的意思是如果文件不存在就创建，如果存在就在内容后面操作
print('helloworld', file = fp)
fp.close()

#不换行输出
print('hello', 'world', 'Python')
