import sys
from collections import deque
#sys.stdin=open("input.txt", "r")
#최단거리 문제는 무조건 bfs 로하는게 한번에 하는게(돌아가지 않음)
dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]
board=[list(map(int, input().split())) for _ in range(7)]
dis=[[0]*7 for _ in range(7)]
Q=deque()
Q.append((0, 0))    #맨 첫 지점
board[0][0]=1       #방문한 곳은 1로 체크해 둠.(벽으로 만들고)
while Q:            #큐가 비면 멈추는거.큐가 뭔가가 있으면 참
    tmp=Q.popleft() #하나 좌표가 빠짐(맨 왼쪽에 있는 =맨 앞에있는)
    for i in range(4):  #4방향 탐색하는거
        x=tmp[0]+dx[i]
        y=tmp[1]+dy[i]  #이렇게하면서 방향봄, 12시방향, 3시방향 6시방향 이렇게 봄
        if 0<=x<=6 and 0<=y<=6 and board[x][y]==0:
            #0<=x<=6 이래야 경계선 밖으로 안 나감. (y도 마찬가지)
            #그리고 벽이면 가지 말아야됨.(1이면 안가야.)
            board[x][y]=1   #
            dis[x][y]=dis[tmp[0]][tmp[1]]+1
            #
            Q.append((x, y))
            #큐에다 넣는거.

if dis[6][6]==0:
    print(-1)
else:
    print(dis[6][6])

#보통 같은 미로문제라도 최단거리 찾는건 bfs,
#경우의 수 찾는건 dfs로 해결하는 경우가 많다.