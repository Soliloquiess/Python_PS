K, N, M = map(int, input().split())

# 필요한 총 금액 계산
required_money = K * N

# 부족한 금액 계산 및 출력
if required_money > M:
    print(required_money - M)
else:
    print(0)

# K, N, M = map(int, input().split())

# 필요한 총 금액 계산
#required_money = K * N

# 부족한 금액 계산
#needed_money = max(0, required_money - M)

#print(needed_money)
