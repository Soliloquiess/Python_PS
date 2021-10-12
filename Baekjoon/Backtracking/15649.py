n, m = list(map(int, input().split()))
s = []

def dfs():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return

    for i in range(1, n + 1):
        if i not in s:
            s.append(i)
            dfs()
            s.pop()
dfs()

# n, m = map(int, input().split())
#
# def f(s):
#   if len(s) == m:
#     print(' '.join(map(str, s)))
#     return
#
#   for i in range(1, n + 1):
#     if i in s:
#       continue
#     f(s + [i])
#
# f([])

# https://jiwon-coding.tistory.com/21?category=882771
# https://jamesu.dev/posts/2020/04/13/baekjoon-problem-solving-15649/