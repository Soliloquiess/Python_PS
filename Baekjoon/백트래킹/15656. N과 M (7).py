N, M = map(int, input().split())
L = list(map(int, input().split()))

L.sort()
out = []

def solve(depth, N, M):
    if depth == M:
        print(' '.join(map(str, out)))
        return
    for i in range(N):
        out.append(L[i])
        solve(depth+1, N, M)
        out.pop()

solve(0, N, M)

#얘도 마찬가지로 3번이 1번에서 if문 제거한거랑 같다.
# https://wlstyql.tistory.com/64?category=852442

# n, m = map(int, input().split())
# num_list = list(map(int, input().split()))
# num_list.sort()
#
# a = [0 for i in range(m)]
# c = [False for i in range(n)]
#
# def go(idx, n, m):
#     if idx == m:
#         print(' '.join(map(str, a)))
#         return
#     for i in range(n):
#         a[idx] = num_list[i]
#         go(idx + 1, n, m)
#     # a[selected] = num_list[idx]
#     # go(idx, selected + 1, n, m)
#     # a[selected] = 0
#     # go(idx + 1, selected, n, m)
#
# go(0, n, m)


# from itertools import product
#
# n,m=map(int,input().split())
# a=list(map(int,input().split()))
# a.sort()
#
# a=product(a, repeat=m)
#
# for i in a:
#     print(*i)

#https://it-garden.tistory.com/159?category=845077