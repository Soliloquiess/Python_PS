N = int(input())
cards = list(map(int, input().split()))
M = int(input())
queries = list(map(int, input().split()))

# 상근이가 가진 카드들의 빈도 계산
card_count = {}
for card in cards:
    if card in card_count:
        card_count[card] += 1
    else:
        card_count[card] = 1

# 쿼리 처리
result = []
for i in queries:
    if i in card_count:
        result.append(card_count[i])
    else:
        result.append(0)

# 결과 출력
print(' '.join(map(str, result)))

# # 입력 받기
# import sys
# input = sys.stdin.read
# data = input().split()
# 
# N = int(data[0])
# cards = list(map(int, data[1:N+1]))
# M = int(data[N+1])
# queries = list(map(int, data[N+2:N+2+M]))
# 
# # 상근이가 가진 카드들의 빈도 계산
# card_count = {}
# for card in cards:
#     if card in card_count:
#         card_count[card] += 1
#     else:
#         card_count[card] = 1
# 
# # 쿼리 처리
# result = []
# for query in queries:
#     if query in card_count:
#         result.append(card_count[query])
#     else:
#         result.append(0)
# 
# # 결과 출력
# print(' '.join(map(str, result)))
