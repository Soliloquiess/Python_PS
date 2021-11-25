# 값 입력
N, K = map(int, input().split())
Money = [int(input()) for _ in range(N)]

# 코인 총 개수 입력 변수
num = 0

# 알고리즘
# 큰 값이 있는 뒤의 인덱스부터 계산
for i in range(1, N + 1):  # 1
    coin = Money[-i]  # 2
    if K >= coin:  # 3
        mok = K // coin  # 4
        K -= coin * mok  # 5
        num += mok  # 6

print(num)

# https://yongku.tistory.com/entry/%EB%B0%B1%EC%A4%80-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EB%B0%B1%EC%A4%80-11047%EB%B2%88-%EB%8F%99%EC%A0%84-0Python

# N, K = map(int, input().split())
# coin_lst = list()
# for i in range(N):
#     coin_lst.append(int(input()))
#
# count = 0
# for i in reversed(range(N)):
#     count += K // coin_lst[i]
#     K %= coin_lst[i]
#     if K == 0:
#         break
#
# print(count)

#https://zidarn87.tistory.com/300