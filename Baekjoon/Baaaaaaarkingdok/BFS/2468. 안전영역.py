from collections import deque

n = int(input())
graph = []
max = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] > max:
            max = graph[i][j]  # 그래프의 원소들 중 최댓값을 찾음


def bfs(xPos, yPos, value, visited):
    q = deque()
    q.append((xPos, yPos))
    visited[xPos][yPos] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] > value and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append((nx, ny))


maximum = 0
for a in range(max):  # 비가 안오는 경우인 0부터 max-1까지 조회(max는 모든 지역이 물에 잠기므로 안전영역이 0임 고려할 필요가 없음)
    #꼭 숫자가 높다고 혹은 낮다고 안전지역이 많이 만들어 지는 것이 아니다!
    #이거 이해 못해서 존나 시간 날렸네 시발.
    visited = [[0] * n for _ in range(n)]  # 매 높이마다 조회를 해야하므로 visited를 매번 정의
    ans = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] > a and visited[i][j] == 0:  # 비가 온것보다 높은 곳이고 방문하지 않은 경우 bfs호출
                bfs(i, j, a, visited)
                ans += 1
    if maximum < ans:
        maximum = ans
print(maximum)

# dir=[[-1,0],[0,1],[1,0],[0,-1]]
# def bfs(start):
#     que = []
#     que.append(start)
#     map_b[start[0]][start[1]] = 0
#     while que:
#         cur = que.pop(0)
#         for k in range(4):
#             nr = cur[0] + dir[k][0]
#             nc = cur[1] + dir[k][1]
#             if nr <0 or nr >= N or nc < 0 or nc >=N:continue
#             if map_b[nr][nc]==0: continue
#             que.append([nr,nc])
#             map_b[nr][nc] = 0
#
#
# N = int(input())
# Map = [list(map(int,input().split())) for _ in range(N)]
# maxT = 0
# ans = 0
# #가장 높은 지대 찾기
# for i in range(N):
#     for j in range(N):
#         maxT = max(maxT,Map[i][j])
# if maxT==1: #최대 영역이 1이라면 전체가 한덩이이므로 답은 1
#     ans =1
# else:
#     for day in range(maxT+1):
#         map_b = [[0]*N for _ in range(N)]
#         for i in range(N):
#             for j in range(N):
#                 map_b[i][j] = 1 if Map[i][j] >= day else 0  #잠긴부분 :0 /잠기지 않은 부분 :1 로 나눔
#         # for row in map_b:
#         #     print(row)
#
#         cnt = 0 #안전영역 갯수
#         for i in range(N):
#             for j in range(N):
#                 if map_b[i][j] ==1:
#                     bfs([i,j])  #bfs로 탐색한 횟수를 알아내서 영역 개수 탐색
#                     cnt+=1
#         ans = max(ans,cnt)
# print('{}'.format(ans))