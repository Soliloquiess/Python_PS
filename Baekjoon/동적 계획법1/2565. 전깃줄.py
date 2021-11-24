N = int(input())

lineList = []

for _ in range(N):
    lineList.append(list(map(int, input().split())))

lineList.sort()

dp = [1]*N
for i in range(N):
    for j in range(i):
        if lineList[i][1] > lineList[j][1] and dp[i] < dp[j]+1:
            dp[i] = dp[j] + 1

print(N-max(dp))


#https://kyoung-jnn.tistory.com/entry/%EB%B0%B1%EC%A4%802565%EB%B2%88%ED%8C%8C%EC%9D%B4%EC%8D%ACPython-%EC%A0%84%EA%B9%83%EC%A4%84-DP

# from sys import stdin
#
#
# n = int(stdin.readline())
#
# lines = []
#
# for _ in range(n):
#     a, b = map(int, stdin.readline().split())
#
#     lines.append((a, b))
#
# lines.sort()
#
# # a 전깃줄 번호를 기준으로 오름차순 정렬된 b 전깃줄 번호의 수열
# a_to_b = list(map(lambda x: x[1], lines))
#
# # LIS 알고리즘 구현
# max_length = [1] * n
#
# for i in range(1, n):
#     for j in range(i):
#         if a_to_b[i] > a_to_b[j]:
#             max_length[i] = max(max_length[i], max_length[j] + 1)
#
# # 없애야 하는 전깃줄의 최소 개수 = 현재 전깃줄의 개수 - 겹치치 않는 최대 전깃줄의 개수
# print(n - max(max_length))

# https://velog.io/@ready2start/Python-%EB%B0%B1%EC%A4%80-2565-%EC%A0%84%EA%B9%83%EC%A4%84