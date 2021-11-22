N, M = map(int, input().split())
L = list(map(int, input().split()))

L.sort()
out = []

def solve(depth, N, M):
    if depth == M:
        print(' '.join(map(str, out)))
        return
    overlap = 0
    for i in range(N):
        if overlap != L[i]:
            out.append(L[i])
            overlap = L[i]
            solve(depth+1, N, M)
            out.pop()

solve(0, N, M)

# n, m = map(int, input().split())
# num_list = list(map(int, input().split()))
# num_list = list(set(num_list))
# num_list.sort()
#
# anses = []
# a = [0 for i in range(m)]
#
# def go(selected, m):
#     if selected == m:
#         anses.append(' '.join(map(str, a)))
#         return
#     for i in range(len(num_list)):
#         a[selected] = num_list[i]
#         go(selected + 1, m)
#
#
# go(0, m)
# print(anses[0])
# for i in range(1, len(anses)):
#     if anses[i - 1] != anses[i]:
#         print(anses[i])

# https://hjp845.tistory.com/87?category=859229


# from itertools import product
#
# n,m=map(int,input().split())
#
# a=list(map(int,input().split()))
# a.sort()
# a=list(product(a, repeat=m))
#
# a=sorted(list(set(a)))
#
# for i in a:
#     print(*i)

# https://it-garden.tistory.com/163?category=845077
