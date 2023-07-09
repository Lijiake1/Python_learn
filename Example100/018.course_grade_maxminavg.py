# Python学习
# 学习时间：2022/9/21 19:01
# 计算学生成绩的最大值和最小值以及平均值

# key: course, value: grade list
course_grades = {}
test_result = []
with open("./input_data/course_student_grade_input.txt", encoding='utf-8') as fin:
    for line in fin:
        # 将每一行最后面的换行符分割掉
        line = line[:-1]
        course, sno, sname, grade = line.split("，")
        if course not in course_grades:
            course_grades[course] = []
        course_grades[course].append(int(grade))

print(course_grades)

for course, grade in course_grades.items():
    print(
        course,
        max(grade),
        min(grade),
        sum(grade) / len(grade)
    )
