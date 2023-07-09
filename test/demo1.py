# Python学习
# 学习时间：2022/8/26 10:08
# 使用print方式进行输出

fp = open('F:/test.txt', 'r')
#print('奋斗成就更好的你', file=fp)
print(fp.readlines())
fp.close()

# 第二种方式，使用文件的读写方式
with open('F:/test.txt', 'a+') as file:
    file.write('奋斗成就更好的你')
