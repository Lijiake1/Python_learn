# Python学习
# 学习时间：2022/9/14 13:06
# 统计一个英语文章中出现最多的单词数

# 定义一个字典，key为单词，value为每个单词出现的次数
word_count = {}

# 打开文件
with open('./input_data/Beginner Guide to Python.txt') as fin:
    for line in fin:
        # 读取每一行并将最后的换行符删除
        line = line[:-1]
        # 将每一行的单词分割开
        words = line.split()
        # 遍历每一个单词
        for word in words:
            # 如果字典里面没有这个单词的key那么久创建一个
            if word not in word_count:
                word_count[word] = 0
            # 将这个单词的次数加一
            word_count[word] += 1

print(word_count)
print(
sorted(
    word_count.items(),
    key=lambda x: x[1],
    reverse=True
)[:10]
)
