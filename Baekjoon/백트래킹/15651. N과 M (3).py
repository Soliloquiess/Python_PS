n, m = map(int, input().split())

s = []


def dfs():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return

    for i in range(1, n + 1):
        s.append(i)
        dfs()
        s.pop()


dfs()


# 이 문제는 15649번과 동일하지만, 중복을 허용하기 떄문에, 10번의 for문에서 중복을 확인하는 if문이 삭제되었다.
# 나머지는 15649번 문제와 동일하다.


#https://jiwon-coding.tistory.com/23?category=882771

# n, m = map(int, input().split())
#
# a = [0 for i in range(m)]
#
# def go(selected, n, m):
#     if selected == m:
#         print(' '.join(map(str, a)))
#         return
#     for i in range(1, n + 1):
#         a[selected] = i
#         go(selected + 1, n, m)
#
# go(0, n, m)
#https://hjp845.tistory.com/79?category=859229

# from itertools import product
#
# n,m=map(int,input().split())
#
# a=product(range(1,n+1),repeat=m)
#
# for i in a:
#     print(*i)
# https://it-garden.tistory.com/155?category=845077