# 시험 본 과목의 개수 N을 입력받습니다.
N = int(input())

# 세준이의 현재 성적을 입력받습니다.
scores = list(map(int, input().split()))

# 성적 중 최댓값을 구합니다.
max_score = max(scores)

# 모든 성적을 변환합니다.
new_scores = [(score / max_score) * 100 for score in scores]

# 변환된 성적의 평균을 계산합니다.
average_score = sum(new_scores) / N

# 결과를 출력합니다.
print(average_score)


# # 시험 본 과목의 개수 N을 입력받습니다.
# N = int(input())
# 
# # 세준이의 현재 성적을 입력받습니다.
# scores = list(map(int, input().split()))
# 
# # 성적 중 최댓값을 구합니다.
# max_score = max(scores)
# 
# # 모든 성적을 변환합니다.
# new_scores = []
# for score in scores:
#     new_scores.append((score / max_score) * 100)
# 
# # 변환된 성적의 평균을 계산합니다.
# total = 0
# for score in new_scores:
#     total += score
# 
# average_score = total / N
# 
# # 결과를 출력합니다.
# print(average_score)
