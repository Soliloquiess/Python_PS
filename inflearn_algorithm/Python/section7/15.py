import sys
from collections import deque
#sys.stdin=open("input.txt", "r")

dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]#12,3,6,9

n, m=map(int, input().split())
board=[list(map(int, input().split())) for _ in range(m)]
Q=deque()
dis=[[0]*n for _ in range(m)]

for i in range(m):  #행
    for j in range(n):  #역
        if board[i][j]==1:  #1은 익은 토마토
            Q.append((i, j))    #이 좌표를 큐에 삽입.   (그 좌표에서 시작해서 퍼져나갈거)

while Q:    #큐면 하나 꺼냄(큐가 비어있지 않으면 계속 돔)
    x, y=Q.popleft()    #하나 꺼냄

    for i in range(4):  #4방향 탐색.
        nx=x+dx[i]
        ny=y+dy[i]      #방향 도는거

        if 0<=nx<m and 0<=ny<n and board[nx][ny]==0:
            #board[nx][ny]==0:은 안 익은 토마토(비었거나 익은 토마토면 퍼지면 안됨)
            board[nx][ny]=1 #익은 토마토로 바꿈(재방문 하지 않게 하려고)

            dis[nx][ny]=dis[x][y]+1 #현재지점은(지금 바로나온지점은 [[TMP[0]][tmp[1]]]인데 거기지점값 +1

            #익은토마토에 각 지점에서 퍼져나감.
            Q.append((nx, ny))

flag=1#안익은 토마토 있는지 확인하기위한 플래그

for i in range(m):
    for j in range(n):
        if board[i][j]==0:  #인접한 토마토 다 익게 했는데도 안 익은 토마토 발견시
            flag=0          #플래그를 0으로 바꿈

result=0                    #최대값 찾아야 하니까


if flag==1:                 #1이면 안 익은 토마토 없이 다 익음
    #다 익었으면 2중포문 돌면서 찾는다.
    for i in range(m):      #그럼 또 2중포문 돌면서 최대값 찾는거.
        for j in range(n):
            if dis[i][j]>result:        #dis[i][j]>result
                result=dis[i][j]        #최대값 바꿔주는거
                # 다 익는데 며칠 걸렸는지 dis에서 최대값.
    print(result)
else:   #참이 아니면 안 익은 토마토 있는거니까 -1출력
    print(-1)

#큐에 익은 토마토들 좌표를 넣는다.
#처음 출발위츠는 0, 그리고 큐에서 나온 좌표로 탐색
#board배열과 dis배열로 dis배열에 각 걸리는 시간을 걸린다
#board[xx][yy]=0 이런식이 0일떄만 가는거
# 이미 익은 토마토는 가면 안됨.
# 2차원 리스트 탐색하면서 최대값 찾는다.