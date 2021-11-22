N, M = map(int, input().split())
L = list(map(int, input().split()))

L.sort()
visited = [False] * N
out = []

def solve(depth, N, M):
    if depth == M:
        print(' '.join(map(str, out)))
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            out.append(L[i])
            solve(depth+1, N, M)
            out.pop()
            visited[i] = False

solve(0, N, M)

#https://wlstyql.   tistory.com/62


# n, m = map(int, input().split())
#
# num_list = list(map(int, input().split()))
# num_list.sort()
# a = [0 for i in range(m)]
# c = [False for i in range(n)]
#
# def go(selected, n, m):
#     if selected == m:
#         print(' '.join(map(str, a)))
#         return
#     for i in range(n):
#         if c[i] == False:
#             c[i] = True
#             a[selected] = num_list[i]
#             go(selected + 1, n, m)
#             c[i] = False
#
#     # a[selected] = num_list[idx]
#     # go(idx + 1, selected + 1, n, m)
#     # a[selected] = 0
#     # go(idx + 1, selected, n, m)
#
# go(0, n, m)

# from itertools import permutations
#
# n,m=map(int,input().split())
#
# a=list(map(int,input().split()))
# a.sort()
#
# a=list(permutations(a,m))
#
# for i in a:
#     print(*i)

#https://it-garden.tistory.com/157?category=845077