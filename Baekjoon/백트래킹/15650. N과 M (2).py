# 15650번
n, m = list(map(int, input().split()))
s = []


def dfs(start):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return

    for i in range(start, n + 1):
        if i not in s:
            s.append(i)
            dfs(i + 1)
            s.pop()


dfs(1)

# https://jiwon-coding.tistory.com/22?category=882771


# n, m = map(int, input().split())
#
# subs = [0 for i in range(m)]
#
# def go(idx, selected, n, m):
#     # 길이 채워지면 종료
#     if selected == m:
#         print(' '.join(map(str, subs)))
#         return
#     # n 초과하면 정수 범위 벗어나는거니까 종료
#     if idx > n:
#         return
#     # 그 idx를 선택한다면 subs에 넣기
#     subs[selected] = idx
#     go(idx + 1, selected + 1, n, m)
#     # 그 idx를 선택하지 않았을 때
#     subs[selected] = 0
#     go(idx + 1, selected, n, m)
#
# go(1, 0, n, m)
# #https://hjp845.tistory.com/78?category=859229


# from itertools import combinations
#
# n,m=map(int,input().split())
#
# a=combinations(range(1,n+1), m)
#
# for i in a:
#     print(*i)
#https://it-garden.tistory.com/154?category=845077