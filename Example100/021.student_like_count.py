# Python学习
# 学习时间：2022/9/25 16:33
# 将文件student_like.txt中的每种兴趣进行统计

# 定义一个字典，key就是兴趣，value就是人数
like_count = {}
# 打开文件
with open("./input_data/student_like.txt", encoding="utf-8") as fin:
    for line in fin:
        line = line[:-1]
        # 将里面的每一个人名和爱好分别保存
        sname, likes = line.split()
        # 将爱好分别存放在列表中
        like_list = likes.split("，")
        # 遍历每一个列表的数据
        for like in like_list:
            # 如果字典中有这个兴趣的key则跳过，如果不存在则创建
            if like not in like_count:
                like_count[like] = 0
            # 将字典中的这个兴趣人数加一
            like_count[like] += 1

print(like_count)
