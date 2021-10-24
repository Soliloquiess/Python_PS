from collections import deque
import copy

m, n, h = map(int, input().split())
graph = [[] for _ in range(h)]

dx = [0,0,0,0,1,-1]
dy = [0,0,1,-1,0,0]
dz = [1,-1,0,0,0,0]

next_queue = deque()
count = 0
flag = 0

for i in range(h):
    for j in range(n):
        graph[i].append(list(map(int, input().split())))

def find_start():
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if graph[i][j][k] == 1:
                    next_queue.append((i, j, k))

def bfs():
    global count
    today_queue = copy.deepcopy(next_queue)

    while today_queue:
        x, y, z = today_queue.popleft()
        next_queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if nx < 0 or nx >= h or ny < 0 or ny >= n or nz < 0 or nz >= m:
                continue
            if graph[nx][ny][nz] == 0:
                graph[nx][ny][nz] = 1
                next_queue.append((nx, ny, nz))
    count += 1


find_start()
while next_queue:
    bfs()

for i in range(h):
    for j in range(n):
        if 0 in graph[i][j]:
            flag = 1

if flag == 1:
    print(-1)
else:
    print(count-1)

#https://hongcoding.tistory.com/16?category=924371


# import sys
# from collections import deque
#
# # input = sys.stdin.readline
#
# M, N, H = map(int, input().split())
#
# floors = []
#
# for _ in range(H):
#     floor = []
#     for _ in range(N):
#         floor.append(list(map(int, input().split())))
#
#     floors.append(floor)
#
# queue = deque()
#
# for i in range(H):
#     for j in range(N):
#         for k in range(M):
#             if (floors[i][j][k] == 1):
#                 queue.append([i, j, k])
#
# # 이전 문제랑 다른 점은 높이가 추가됨
# dx = [1, -1, 0, 0, 0, 0]
# dy = [0, 0, 1, -1, 0, 0]
# dh = [0, 0, 0, 0, 1, -1]
#
# while queue:
#     height, row, col = queue.popleft()
#
#     for k in range(6):
#         _height = height + dh[k]
#         _row = row + dy[k]
#         _col = col + dx[k]
#
#         if 0 <= _height < H and 0 <= _row < N and 0 <= _col < M and floors[_height][_row][_col] == 0:
#             queue.append([_height, _row, _col])
#             floors[_height][_row][_col] = floors[height][row][col] + 1
#
# check_tot = False
# result = -2
#
# for i in floors:
#     for j in i:
#         for k in j:
#             if (k == 0):
#                 check_tot = True
#             result = max(result, k)
#
# if check_tot:
#     print(-1)
# elif (result == -1):
#     print(0)
# else:
#     print(result - 1)

# https://hwiyong.tistory.com/390

# https://alpyrithm.tistory.com/241
# https://it-garden.tistory.com/190
# https://hongcoding.tistory.com/16?category=924371