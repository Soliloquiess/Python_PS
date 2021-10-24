from collections import deque

m, n = map(int, input().split())
graph = []
queue = deque([])
for i in range(n):
    graph.append(list(map(int, input().split())))

    for j in range(m):  # 익은 토마토 큐에 저장
        if graph[i][j] == 1:
            queue.append([i, j])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            a = x + dx[i]
            b = y + dy[i]
            if 0 <= a < n and 0 <= b < m and graph[a][b] == 0:
                queue.append([a, b])
                graph[a][b] = graph[x][y] + 1   # 그래프 해당 위치 에서 갈수 있는 경우.

bfs()
answ = 0
for i in graph:
    for j in i:
        if j == 0:
            print(-1)   #만약 0인 부분이 있으면 -1 출력하고 바로 종료시킨다.
            exit(0)
    answ = max(answ, max(i))
print(answ - 1)
