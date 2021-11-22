N, M = map(int, input().split())
L = list(map(int, input().split()))

L.sort()
visited = [False] * N
out = []

def solve(depth, idx, N, M):
    if depth == M:
        print(' '.join(map(str, out)))
        return
    for i in range(idx, N):
        if not visited[i]:
            visited[i] = True
            out.append(L[i])
            solve(depth+1, i+1, N, M)
            out.pop()
            visited[i] = False

solve(0, 0, N, M)

#https://wlstyql.tistory.com/63?category=852442

# n, m = map(int , input().split())
#
# num_list = list(map(int, input().split()))
# num_list.sort()
#
# a = [0 for i in range(m)]
#
# def go(idx, selected, n, m):
#     if selected == m:
#         print(' '.join(map(str, a)))
#         return
#     if idx == n:
#         return
#     a[selected] = num_list[idx]
#     go(idx + 1, selected + 1, n, m)
#     a[selected] = 0
#     go(idx + 1, selected, n, m)
#
# go(0, 0, n, m)

# from itertools import combinations
#
# n,m=map(int,input().split())
#
# a=list(map(int,input().split()))
#
# a.sort()
#
# a=list(combinations(a, m))
#
# for i in a:
#     print(*i)

# https://it-garden.tistory.com/158?category=845077