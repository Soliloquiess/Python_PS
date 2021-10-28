n, m = map(int, input().split())

s = []


def dfs(start):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return

    for i in range(start, n + 1):
        s.append(i)
        dfs(i)
        s.pop()


dfs(1)

#https://jiwon-coding.tistory.com/24?category=882771


# n, m = map(int, input().split())
#
# a = [0 for i in range(m)]
#
# def go(number, selected, n, m):
#     if selected == m:
#         print(' '.join(map(str, a)))
#         return
#     if number > n:
#         return
#     a[selected] = number
#     go(number, selected + 1, n, m)
#     a[selected] = 0
#     go(number + 1, selected, n, m)
#
# go(1, 0, n, m)
#https://hjp845.tistory.com/80?category=859229

# from itertools import combinations_with_replacement
#
# n,m=map(int,input().split())
#
# a=combinations_with_replacement(range(1,n+1),m)
#
# for i in a:
#     print(*i)

#https://it-garden.tistory.com/156?category=845077