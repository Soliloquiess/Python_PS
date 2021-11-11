import sys
from collections import deque
#sys.stdin=open("input.txt", "r")

#최단거리 문제가 아님.
#dfs로 모든 경우 찾는거 쭉 벋어가서 도착점까지 가고 다른길 찾아보고 하는거.
dx=[-1, 0, 1, 0]    #행(세로)
dy=[0, 1, 0, -1]    #열(가로)
def DFS(x, y):
    global cnt
    if x==6 and y==6:   #도착지점 온거. 그럼 카운팅
        cnt+=1
    else:
        for i in range(4):  #4방향으로 뻗음.
            xx=x+dx[i]      #xx는 x에 넘어온거
            yy=y+dy[i]      #yy는 앞으로 갈 방향(xx,yy)
            #4방향 탐색

            if 0<=xx<=6 and 0<=yy<=6 and board[xx][yy]==0:
                #격자판의 밖으로 나가면 안 된다.
                # board[xx][yy]==0이 부분은 방문을 안했어야 됨. 방문했던 경로면 안됨.
                board[xx][yy]=1#벽으로 체크함.
                DFS(xx, yy) #뻗어나감
                board[xx][yy]=0 #백으로 뒤돌아감(벽 취소해줌)
                #뒤로 백할떄는 통로로 만들어줘야 다른 길을 찾을 수가 있다.
    return cnt;
if __name__=="__main__":
    board=[list(map(int, input().split())) for _ in range(7)]
    cnt=0
    board[0][0]=1#  방문한 곳은 벽으로 만듬.
    print(DFS(0, 0)) #출발지점.
    print(cnt)
