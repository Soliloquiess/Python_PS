import sys
input = sys.stdin.readline

# make dp
dp = []
dp.append([1 for i in range(10)])
for i in range(99):
  dp.append([0 for i in range(10)])

# iterate dp
for i in range(99):
  for j in range(10):
    if j >= 1:
      dp[i+1][j-1] += dp[i][j]
    if j <= 8:
      dp[i+1][j+1] += dp[i][j]

# input & output
n = int(input())
print((sum(dp[n-1])-dp[n-1][0])%1000000000)

# N = int(input())
#
# dp = [[0]*10 for _ in range(N+1)]
# for i in range(1, 10):
#     dp[1][i] = 1
#
# MOD = 1000000000
#
# for i in range(2, N+1):
#     for j in range(10):
#         if j == 0:
#             dp[i][j] = dp[i-1][1]
#         elif j == 9:
#             dp[i][j] = dp[i-1][8]
#         else:
#             dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
#
# print(sum(dp[N]) % MOD)

# https://cotak.tistory.com/12


# from sys import stdin
#
# n = int(stdin.readline())
#
# stairs = [[0] * 10 for _ in range(n + 1)]
#
# # 초기값 설정
# stairs[1] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
#
# for i in range(2, n + 1):
#     # 계단 수가 0으로 끝나는 경우
#     stairs[i][0] = stairs[i - 1][1]
#     # 계단 수가 9로 끝나는 경우
#     stairs[i][9] = stairs[i - 1][8]
#
#     # 계단 수가 1~8로 끝나는 경우
#     for j in range(1, 9):
#         stairs[i][j] = stairs[i - 1][j - 1] + stairs[i - 1][j + 1]
#
# print(sum(stairs[n]) % 1000000000)

# https://velog.io/@ready2start/Python-%EB%B0%B1%EC%A4%80-10844-%EC%89%AC%EC%9A%B4-%EA%B3%84%EB%8B%A8-%EC%88%98

# import sys
# input = sys.stdin.readline
#
# # make dp
# dp = []
# dp.append([1 for i in range(10)])
# for i in range(99):
#   dp.append([0 for i in range(10)])
#
# # iterate dp
# for i in range(99):
#   for j in range(10):
#     if j >= 1:
#       dp[i+1][j-1] += dp[i][j]
#     if j <= 8:
#       dp[i+1][j+1] += dp[i][j]
#
# # input & output
# n = int(input())
# print((sum(dp[n-1])-dp[n-1][0])%1000000000)

#https://dev-wd.github.io/algorithm/backjoon10844/