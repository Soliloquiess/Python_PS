import sys

#sys.stdin = open("input.txt", "r")

#DFS 는 상태트리만 잘 구성하면 된다.
def DFS(v):
    if v == n + 1:      #3이면  4가 종착지였으니까 종료지점이므로 출력.
        for i in range(1, n + 1):   #n까지니까 n+1까지 해서 n까지 돌게하는거
            if ch[i] == 1:  #인덱스를 체크하는거
                print(i, end=' ')
        print()
    else:
        ch[v] = 1   #사용하는거로 두면
        DFS(v + 1)
        ch[v] = 0   #사용하지 않는거로 두면
        DFS(v + 1)


if __name__ == "__main__":
    n = int(input())
    ch = [0] * (n + 1)#체크변수 만드는 거(0으로 처음엔 초기화되는), 원소를 1부터 쓸거니까 n+1로 두자
    DFS(1)


