import sys
#sys.stdin=open("input.txt", "r")
dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]

def DFS(x, y):
    global cnt
    cnt+=1  #하나의 집 좌표 넘어오면 카운팅
    board[x][y]=0   #방문하면 0으로 바꿔주자.(여러번 방문하면 안되므로)

    for i in range(4):  #4방향
        xx=x+dx[i]
        yy=y+dy[i]
        if 0<=xx<n and 0<=yy<n and board[xx][yy]==1: #1이여야지 집이니까 뻗어나가는거.
            DFS(xx, yy)
    return cnt;

if __name__=="__main__":
    n=int(input())
    board=[list(map(int, input())) for _ in range(n)]
    res=[]
    for i in range(n):
        for j in range(n):
            if board[i][j]==1:  #이러면 집 발견 여기서 부터 퍼져 나가야 됨.
                cnt=0#집의 개수를 카운팅
                # print(DFS(i, j))  # 여기서부터 집의 개수 퍼져나감

                DFS(i, j) #여기서부터 집의 개수 퍼져나감
                # cnt가 발견될떄마다 0으로 하고 dfs호출
                res.append(cnt) #cnt개수 구해졌으면  res에 추가.
    print(len(res))
    res.sort()
    for x in res:
        print(x)

#1을 카운팅 하면서 4방향 탐색하면서 1이면 0으로 바꿔줌(다시 방문 못하도록)
#