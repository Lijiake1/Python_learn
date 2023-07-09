# Python学习
# 学习时间：2022/9/22 13:21
"""通过查询course_teacher.txt找到每一个课程的老师，
    然后将相关的信息与course_student_grade_input.txt中的学生信息关联起来
"""

# 初始化一个字典来保存课程与老师的对应关系
course_teacher_map = {}
# 打开课程和老师对应的文件，并将对应关系保存在字典中
with open("./input_data/course_teacher.txt", encoding="utf-8") as fin:
    for line in fin:
        line = line[:-1]
        course, teacher = line.split("，")
        course_teacher_map[course] = teacher
# 初始化一个列表来保存合并后的学生信息文件
course_student_teacher = []
# 打开文件并将学生信息保存在列表中同时加上相应课程的教师信息
with open("./input_data/course_student_grade_input.txt", encoding="utf-8") as fin:
    for line in fin:
        line = line[:-1]
        course, sno, sname, sgrade = line.split("，")
        teacher = course_teacher_map.get(course)
        course_student_teacher.append(f"{course}, {teacher}, {sno}, {sname}, {sgrade}")

# 将列表中的内容保存在一个新的文件中
with open("./input_data/course_student_teacher.txt", "w", encoding="utf-8") as wfile:
    for item in course_student_teacher:
        wfile.write(item + '\n')


