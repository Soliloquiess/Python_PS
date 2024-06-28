N, k = map(int, input().split())
scores = list(map(int, input().split()))

# 점수를 내림차순으로 정렬
scores.sort(reverse=True)

# 커트라인 점수는 상을 받는 사람들 중 가장 낮은 점수
cutoff_score = scores[k-1]

print(cutoff_score)



# # 입력값 처리
# N, k = map(int, input().split())
# scores = list(map(int, input().split()))
#
# # 상위 k개의 점수를 저장할 리스트
# top_k_scores = []
#
# # 점수들을 하나씩 비교하면서 top_k_scores를 유지
# for score in scores:
#     if len(top_k_scores) < k:
#         top_k_scores.append(score)
#     else:
#         # 최소값을 찾아서 비교 후 교체
#         min_index = 0
#         for i in range(1, len(top_k_scores)):
#             if top_k_scores[i] < top_k_scores[min_index]:
#                 min_index = i
#         if score > top_k_scores[min_index]:
#             top_k_scores[min_index] = score
#
# # top_k_scores에서 가장 작은 값이 커트라인 점수
# cutoff_score = top_k_scores[0]
# for score in top_k_scores:
#     if score < cutoff_score:
#         cutoff_score = score
#
# print(cutoff_score)
