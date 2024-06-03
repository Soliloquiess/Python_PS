# 모든 학생의 출석번호 리스트를 생성합니다.
all_students = set(range(1, 31))

# 제출한 학생들의 출석번호를 입력받아 집합에 추가합니다.
submitted_students = set()
for _ in range(28):
    n = int(input())
    submitted_students.add(n)

# 제출하지 않은 학생들의 출석번호를 구합니다.
missing_students = sorted(all_students - submitted_students)

# 결과 출력
for student in missing_students:
    print(student)

# # 모든 학생의 출석번호 리스트를 생성합니다.
# all_students = list(range(1, 31))
#
# # 제출한 학생들의 출석번호를 입력받아 리스트에서 제거합니다.
# submitted_students = []
# for _ in range(28):
#     n = int(input())
#     submitted_students.append(n)
#
# # 제출한 학생들을 all_students 리스트에서 제거합니다.
# for student in submitted_students:
#     all_students.remove(student)
#
# # 남은 학생들 (제출하지 않은 학생들)을 정렬합니다.
# # 정렬 알고리즘 사용
# for i in range(len(all_students)):
#     for j in range(i + 1, len(all_students)):
#         if all_students[i] > all_students[j]:
#             all_students[i], all_students[j] = all_students[j], all_students[i]
#
# # 결과 출력
# print(all_students[0])
# print(all_students[1])


# 정렬 알고리즘 안 쓰고

# # 모든 학생의 출석번호 리스트를 생성합니다.
# all_students = list(range(1, 31))
# 
# # 제출한 학생들의 출석번호를 입력받아 리스트에서 제거합니다.
# for _ in range(28):
#     n = int(input())
#     all_students.remove(n)
# 
# # 남은 학생들 (제출하지 않은 학생들)을 변수에 저장합니다.
# missing_student1 = all_students[0]
# missing_student2 = all_students[1]
# 
# # 두 학생 번호를 비교하여 작은 것부터 출력합니다.
# if missing_student1 < missing_student2:
#     print(missing_student1)
#     print(missing_student2)
# else:
#     print(missing_student2)
#     print(missing_student1)
