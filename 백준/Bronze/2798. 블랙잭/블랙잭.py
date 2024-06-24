N, M = map(int, input().split())
cards = list(map(int, input().split()))

# 초기값 설정
best_sum = 0

# 모든 세 카드의 조합을 검사
for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            current_sum = cards[i] + cards[j] + cards[k]
            if current_sum <= M and current_sum > best_sum:
                best_sum = current_sum

# 결과 출력
print(best_sum)
