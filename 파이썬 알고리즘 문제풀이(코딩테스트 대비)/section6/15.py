import sys
#sys.stdin = open("input.txt", "r")

def DFS(v):
    global cnt, path
    if v == n:  #n에 오면 종착지점에 옴
        cnt += 1
        for x in path:
            print(x, end=' ')
        print()
    else:    #for문으로 가지 뻗어야
        for i in range(1, n + 1):   #0번부터 도는게 아니라 1번부터 돌아야(n가지 가지 뻗음)
            if g[v][i] == 1 and ch[i] == 0: #i가 방문하려는 노드, ch[i] == 0은 방문 안한거
                #현재 있는 노드가 v노드 여기서 i번 노드로 갈 수 있는지 물어봄.
                ch[i] = 1   #방문했다고 체크 검
                path.append(i)  #v에서 i로 넘어감.
                DFS(i)      #v에서 i로 이동하니까 i는 현재 노드가 됨.
                path.pop()  #뒤로 백 했을떈 pop 해줘야됨!
                ch[i] = 0   #호출한걸 뒤로 빽하는거라 체크 0으로 풀어줌.(이거 꼭 해야됨)


if __name__ == "__main__":
    n, m = map(int, input().split())
    g = [[0] * (n + 1) for _ in range(n + 1)]   #둘다 1번부터 n번까지니까 n+1로 만듬.
    ch = [0] * (n + 1)
    for i in range(m):  #  m개의 간선정보 읽어서
        a, b = map(int, input().split())    #두개 넣어서
        g[a][b] = 1     #이동할수 있는거 체크함(방향그래프니까 하나만)
    cnt = 0
    ch[1] = 1           #그 노드 방문했다 체크하고 감
    path = list()       #경로 저장할 리스트
    # path = [] 이렇게 해도 동일한 리스트 생성하는 법

    path.append(1)      #1번에서 출발하니까 이건 무조건 넣어줘야(리스트 처음은 무조건 1 들감.
    DFS(1)
    print(cnt)