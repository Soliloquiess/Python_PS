# import sys
# from itertools import combinations
#
# input = sys.stdin.readline
#
# N = int(input())
# arr = []
# for _ in range(N):
#     _input = list(map(int, input().split()))
#     arr.append(_input)
#
# candidate = [i for i in range(N)]
# result = sys.maxsize
# for comb in combinations(candidate, N // 2):
#     start = set(comb)
#     link = set(candidate) - start
#     start = list(start)
#     link = list(link)
#
#     score = 0
#     for i in range(1, N // 2):
#         for j in range(i):
#             score += arr[start[i]][start[j]] + arr[start[j]][start[i]]
#             score -= arr[link[i]][link[j]] + arr[link[j]][link[i]]
#     result = min(abs(score), result)
#
# print(result)

#https://hillier.tistory.com/75

import sys

input = sys.stdin.readline

def dfs(idx, cnt):
    global ans
    if cnt == n // 2:
        start, link = 0, 0
        for i in range(n):
            for j in range(n):
                if select[i] and select[j]:
                    start += a[i][j]
                elif not select[i] and not select[j]:
                    link += a[i][j]
        ans = min(ans, abs(start - link))

    for i in range(idx, n):
        if select[i]:
            continue
        select[i] = 1
        dfs(i + 1, cnt + 1)
        select[i] = 0


n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

select = [0 for _ in range(n)]
ans = sys.maxsize
dfs(0, 0)
print(ans)

#https://chldkato.tistory.com/155