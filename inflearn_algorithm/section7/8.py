import sys
from collections import deque
#섹션2 에있던 사과나무와 똑같은데 이걸 bfs 로 풀어보자.
#sys.stdin = open("input.txt", "r")
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
#12시,3시,6시,9시 방향 탐색

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
ch = [[0] * n for _ in range(n)]
sum = 0
Q = deque()
ch[n // 2][n // 2] = 1  #중앙지점.(중앙을 방문했다고 체크해준다.)
sum += a[n // 2][n // 2] #거길 sum에 누적하고
Q.append((n // 2, n // 2))  #그 부분을 (중앙) 방문했다고 체크함.큐에 넣어두고
L = 0   #레벨 0이다 하고 bfs가 여기서 탐색
while True:
    if L == n // 2: #n이 5라면 L이 2가 되었을 떄, 목표지점으로 옴. L이 2로오면 목표지점온거.
        break
    size = len(Q)   #큐에 쌓인거
    for i in range(size):   #사이즈만큼 돌고
        tmp = Q.popleft()   #하나 나오면 하나 꺼냄
        for j in range(4):  #그럼 거기서 퍼져야됨.(4갈래로 퍼짐
            x = tmp[0] + dx[j]  #
            y = tmp[1] + dy[j]  #4방향을 시계방향으로 돌면서 탐색
            if ch[x][y] == 0:   #탐색한 지정이 0일떄만(방문 안 했을떄만) 1이면 방문한데니까
                sum += a[x][y]  #sum은 a의 [x][y]라는 곳을 누적
                ch[x][y] = 1    #ch에 방문했다고 체크
                Q.append((x, y))
    # print(L,size)
    # for x in ch:
    #     print(x)
    L += 1
print(sum)


#정중앙에서 시작(정사각형 5,5일때 0 1 2 3 4 에서 2,2 시작)
# 그럼 이제 4방향으로 탐색
# (1,2), (2,3), (3,2), (2,1) 로 탐색
#12시 방향, 3시 방향, 6시 방향, 9시 방향.