from collections import deque
import sys
input = sys.stdin.readline
def bfs():
    global q, f
    while q:
        temp = deque()
        while q:    #사람 위치
            x, y = q.popleft()
            if (x == r - 1 or y == c - 1 or x == 0 or y == 0) and s[x][y] != "F":
                return s[x][y] + 1  #x,y가 사람 있던 위치 거기에 범위 벗어나서 탈춯라니까 +1을 리턴하고 함수 종료.

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < r and 0 <= ny < c and s[nx][ny] == "." and s[x][y] != "F": #밖으로 안 나가고 (맨 위 혹은 #가 아니고 불이아닌곳이면 temp에 넣는다.)
                    temp.append([nx, ny])
                    s[nx][ny] = s[x][y] + 1
        q = temp
        if not q:   #큐가 비었으면 종료시킨다.
            break
        temp = deque()  #temp 초기화
        while f:    #불의 위치
            x, y = f.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < r and 0 <= ny < c and visit[nx][ny] == 0 and s[nx][ny] != "#": #0보다 크고 0 <= nx < r and 0 <= ny < c 인 곳은 F로 만들어버린다.0
                    temp.append([nx, ny])   #불의 위치도 temp변수에 넣어줬다.
                    visit[nx][ny] = 1
                    s[nx][ny] = "F"
        f = temp



dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
r, c = map(int, input().split())
s = []
q = deque()
f = deque()
visit = [[0] * c for i in range(r)]
for i in range(r):
    a = list(input().strip())
    s.append(a)
    for j in range(c):
        if a[j] == "J":
            q.append([i, j])
            s[i][j] = 0
        elif a[j] == "F":
            f.append([i, j])
            visit[i][j] = 1 #불난곳 1
result = bfs()
print(result if result != None
      else "IMPOSSIBLE")    #result가 비지 않았으면 result 출력하고 아니면 impossible 출력하라는 의미네.