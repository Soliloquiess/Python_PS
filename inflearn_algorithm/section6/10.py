import sys

#sys.stdin = open("input.txt", "r")


def DFS(L, s):
    global cnt#여기서 글로벌 변수화 꼭 해줘야(안해주면 로컬변수화 되서 답 출력못해)
    if L == m:  #중복순열 할때와 똑같음.
        for i in range(m):
            print(res[i], end=' ')
        print()
        cnt += 1    #이러면 로컬변수화 되니까 글로벌 변수(전역) 으로 해줘야
    else:
        for i in range(s, n + 1):   #s부터 n까지 뻗어야 됨.
           #s~n까지 도는데 4 2에서 만약 5로 가면 돌지않고 그냥 나옴.
            res[L] = i
            DFS(L + 1, i + 1)   #레벨은 1 증가 넘어가는게 i+1(가지 뻗는건 i니까) .  s에 +1하는게 아니다!
            #1부터 n까지 돌고있는건 i.

n, m = map(int, input().split())
res = [0] * (n + 1)
cnt = 0
DFS(0, 1)
print(cnt)


#순열 조합은 매우 중요 순열과 비슷하지만 조합과 순열은 상태트리가 다르다.
#조합은 시작지점이 있어야 한다.