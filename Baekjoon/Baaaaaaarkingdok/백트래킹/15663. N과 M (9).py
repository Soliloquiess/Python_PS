# import sys
#
# N, M = map(int, sys.stdin.readline().split())
# N_list = list(map(int, sys.stdin.readline().split()))
# N_list.sort()
# check = [0 for _ in range(N)]
# answer = []
#
# def NandM9(index, N, M):
#     if index == M:
#         print(' '.join(map(str, answer)))
#         return
#     dup = 0
#     for i in range(N):
#         if not check[i] and N_list[i] != dup:
#             check[i] = 1
#             answer.append(N_list[i])
#             dup = N_list[i]
#             NandM9(index + 1, N, M)
#             answer.pop()
#             check[i] = 0
#
#
# NandM9(0, N, M)

#https://black-hair.tistory.com/60?category=849209


# n, m = map(int, input().split())
# num_list = list(map(int, input().split()))
# num_list.sort()
#
# a = [0 for i in range(m)]
# c = [False for i in range(n)]
# ans = []
#
# def go(idx, n, m):
#     if idx == m:
#         ans.append(a.copy())
#         return
#     for i in range(n):
#         if c[i] == False:
#             c[i] = True
#             a[idx] = num_list[i]
#             go(idx + 1, n, m)
#             c[i] = False
#
# go(0, n, m)
# ans.sort()
# print(' '.join(map(str, ans[0])))
# for i in range(1, len(ans)):
#     if ans[i - 1] != ans[i]:
#         print(' '.join(map(str, ans[i])))

# https://hjp845.tistory.com/85?category=859229


# from itertools import permutations
#
# n,m=map(int,input().split())
#
# a=list(map(int,input().split()))
#
# a=list(permutations(a, m))
#
# a=sorted(list(set(a)))
#
# for i in a:
#     print(*i)
#   https://it-garden.tistory.com/161?category=845077