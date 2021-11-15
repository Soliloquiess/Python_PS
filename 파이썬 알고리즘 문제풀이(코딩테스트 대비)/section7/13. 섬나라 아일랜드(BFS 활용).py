import sys
from collections import deque
#sys.stdin=open("input.txt", "r")

dx=[-1, -1, 0, 1, 1, 1, 0, -1]
dy=[0, 1, 1, 1, 0, -1, -1, -1]  #8방향 (시계방향)

n=int(input()) #격자의 개수 읽음
board=[list(map(int, input().split())) for _ in range(n)]
#보드에 지도 정보 입력받음.

cnt=0   #섬의 개수
Q=deque()   #큐라는 자료구조(덱)
for i in range(n):
    for j in range(n):
        if board[i][j]==1:  #하나의 섬의 한 부분이 발견 됨.(여기서부터 대각선으로 뻗어나감)
            board[i][j]=0   #board[i][j] 최초로 발견된 지점 0으로
            Q.append((i, j))    #여기서 출발
            while Q:            #큐가 도는거 비어있으면 거짓 되서 멈춤
                tmp=Q.popleft() #하나 나옴
                for k in range(8):      #8방향 도는거
                    x=tmp[0]+dx[k]
                    y=tmp[1]+dy[k]
                    if 0<=x<n and 0<=y<n and board[x][y]==1:
                        #x,y가 0보다 크거나 같고 n보다 작아야
                        #board[x][y]==1 이렇게 되있어야 퍼져나감
                        board[x][y]=0
                        Q.append((x, y))
            cnt+=1#섬의 개수 +1
print(cnt)


#이건 단지방향 붙이기와 유사한데 4방향이 아닌 8방향 탐색을 한다.
#대각선도 뻗어나가는 거고 단지 개수 몇개인지 세면 된다.