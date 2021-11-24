import sys

N, K = map(int, input().split())
stuff = [[0, 0]]
knapsack = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

for _ in range(N):
    stuff.append(list(map(int, input().split())))

# 냅색 문제 풀이
for i in range(1, N + 1):
    for j in range(1, K + 1):
        weight = stuff[i][0]
        value = stuff[i][1]

        if j < weight:
            knapsack[i][j] = knapsack[i - 1][j]  # weight보다 작으면 위의 값을 그대로 가져온다
        else:
            knapsack[i][j] = max(value + knapsack[i - 1][j - weight], knapsack[i - 1][j])

print(knapsack[N][K])

#https://claude-u.tistory.com/208

# n, k = map(int, input().split())
#
# thing = [[0,0]]
# d = [[0]*(k+1) for _ in range(n+1)]
#
# for i in range(n):
#     thing.append(list(map(int, input().split())))
#
# for i in range(1, n+1):
#     for j in range(1, k+1):
#         w = thing[i][0]
#         v = thing[i][1]
#
#         if j < w:
#             d[i][j] = d[i-1][j]
#         else:
#             d[i][j] = max(d[i-1][j], d[i-1][j-w]+v)
#
# print(d[n][k])

#https://hongcoding.tistory.com/50