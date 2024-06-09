

dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
a = input()
ret = 0
for j in range(len(a)):
    for i in dial:
        if a[j] in i:
            ret += dial.index(i)+3
print(ret)


# # 다이얼 넘버
# Number = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
#
# #알파벳 입력
# li = list(input())
#
# #걸리는 시간
# result = 0
#
# for i in li :
#     for j in Number :
#         # 만약에 입력받은 값이 Number에 있으면 index에서 3초를 더해준다.
#         if i in j :
#             result += Number.index(j) + 3
#
#
# print(result)


# # 알파벳에 대응하는 다이얼 시간을 미리 딕셔너리에 저장
# dial = {
#     'A': 3, 'B': 3, 'C': 3,
#     'D': 4, 'E': 4, 'F': 4,
#     'G': 5, 'H': 5, 'I': 5,
#     'J': 6, 'K': 6, 'L': 6,
#     'M': 7, 'N': 7, 'O': 7,
#     'P': 8, 'Q': 8, 'R': 8, 'S': 8,
#     'T': 9, 'U': 9, 'V': 9,
#     'W': 10, 'X': 10, 'Y': 10, 'Z': 10
# }
#
# # 입력 받기
# word = input().strip()
#
# # 필요한 시간을 계산
# total_time = 0
# for char in word:
#     total_time += dial[char]
#
# # 결과 출력
# print(total_time)
# 
# # 알파벳을 다이얼 숫자와 매핑하는 리스트
# dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
# 
# # 입력 받기
# word = input().strip()
# 
# # 필요한 시간을 계산
# total_time = 0
# for char in word:
#     for group in dial:
#         if char in group:
#             total_time += dial.index(group) + 3
# 
# # 결과 출력
# print(total_time)
