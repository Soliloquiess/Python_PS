# 등급에 따른 과목 평점
grade_points = {
    'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0,
    'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0.0
}

total_points = 0.0
total_credits = 0.0

# 20개의 과목 정보를 입력 받음
for _ in range(20):
    course = input().strip()
    course_name, credit, grade = course.split()
    credit = float(credit)
    
    if grade == 'P':
        continue
    
    if grade in grade_points:
        total_points += credit * grade_points[grade]
        total_credits += credit

if total_credits == 0:
    gpa = 0.0
else:
    gpa = total_points / total_credits

print(f"{gpa:.4f}")
