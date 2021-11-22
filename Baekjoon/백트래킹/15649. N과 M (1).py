n, m = list(map(int, input().split()))

s = []


def dfs():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return #리턴 안하면 dfs()함수 실행하고 s.pop()을 가는게 아니라(아래 문장 실행이 아니라) 리턴 안하고 for문으로 돌아가서 실행


    for i in range(1, n + 1):
        if i not in s:
            s.append(i)
            dfs()
            s.pop()


dfs()

# 3. 재귀함수를 이용하여 m개의 수열을 저장하기 위한 리스트
#
# 6. 리스트에 들어간 수열들이 m개가 되면 리스트에 들어있는 숫자들을 모두 출력하고 함수를 나온다.
#
# 10. for문을 이용하여 1부터 n까지의 숫자들을 모두 확인
#
# 11. 리스트 s 중복여부 확인
#
# 12. 중복이 아니면 숫자 i를 리스트 s에 넣기
#
# 13. 현재 s=[1]인 상태에서 다음숫자를 넣기위하여 가지치기하기(재귀함수)
#
#   -> 만약 n=4, m=2라면 밑과 같은 형태로 진행될 것이다.
#
#       s : [1] -> [1,2] -> [1] -> [1,3] -> [1] -> [1,4]
#
#                   출력   pop(2)  출력   pop(3)  출력
# https://jiwon-coding.tistory.com/21?category=882771


# n, m = map(int, input().split())
#
# check = [False for i in range(n + 1)]
# subs = [i for i in range(m)]
#
# def go(idx, n, m):
#     if idx == m:
#         print(' '.join(map(str, subs)))
#         return
#     else:
#         for i in range(1, n + 1):
#             if check[i] == False:
#                 check[i] = True
#                 subs[idx] = i
#                 go(idx + 1, n, m)
#                 check[i] = False
#
# go(0, n, m)

# https://hjp845.tistory.com/77?category=859229


# from itertools import permutations
#
# n,m=map(int,input().split())
#
# a=list(permutations(range(1,n+1),m))
#
# for i in a:
#     print(*i)
#
#https://it-garden.tistory.com/153?category=845077