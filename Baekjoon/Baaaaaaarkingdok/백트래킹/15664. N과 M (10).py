# N, M = map(int, input().split())
# L = list(map(int, input().split()))
#
# L.sort()
# visited = [False] * N
# out = []
#
# def solve(depth, idx, N, M):
#     if depth == M:
#         print(' '.join(map(str, out)))
#         return
#     overlap = 0
#     for i in range(idx, N):
#         if not visited[i] and overlap != L[i]:
#             out.append(L[i])
#             visited[i] = True
#             overlap = L[i]
#             solve(depth+1, i+1, N, M)
#             out.pop()
#             visited[i] = False
#
# solve(0, 0, N, M)

#https://wlstyql.tistory.com/68?category=852442
# import sys
#
# N, M = map(int, sys.stdin.readline().split())
# N_list = list(map(int, sys.stdin.readline().split()))
# N_list.sort()
# check = [0 for _ in range(N)]
# answer = []
#
#
# def NandM10(index, start, N, M):
#     if index == M:
#         print(' '.join(map(str, answer)))
#         return
#
#     dup = 0
#     for i in range(start, N):
#         if not check[i] and dup != N_list[i]:
#             answer.append(N_list[i])
#             check[i] = 1
#             dup = N_list[i]
#             NandM10(index + 1, i, N, M)
#             answer.pop()
#             check[i] = 0
#
#
# NandM10(0, 0, N, M)

#https://black-hair.tistory.com/61?category=849209

# n, m = map(int, input().split())
# num_list = list(map(int, input().split()))
# num_list.sort()
#
# anses = []
# a = [0 for i in range(m)]
#
# def go(idx, selected, n, m):
#     if selected == m:
#         if a not in anses:
#             anses.append(a.copy())
#         return
#     if idx == n:
#         return
#     a[selected] = num_list[idx]
#     go(idx + 1, selected + 1, n, m)
#     a[selected] = 0
#     go(idx + 1, selected, n, m)
#
# go(0, 0, n, m)
# for ans in anses:
#     print(' '.join(map(str, ans)))

#https://hjp845.tistory.com/86?category=859229


# from itertools import combinations
# n,m=map(int,input().split())
#
# a=list(map(int,input().split()))
# a.sort()
#
# a=list(combinations(a, m))
# a=sorted(list(set(a)))
#
# for i in a:
#     print(*i)

#https://it-garden.tistory.com/162?category=845077