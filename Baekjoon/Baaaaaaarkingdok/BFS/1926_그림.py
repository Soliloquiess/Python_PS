import sys
from collections import deque

#N-행 M-열
N,M=map(int, sys.stdin.readline().split())

#painting 입력
paint=[list(map(int,sys.stdin.readline().split())) for _ in range(N)]
#방문 체크
visited=[list(False for _ in range(M)) for _ in range(N)]
#상하좌우 체크용(dx,dy)
dx=[-1,1,0,0]
dy=[0,0,-1,1]

#그림크기
def bfs(x,y):
	size=1
	q = deque()
	#시작점
	q.append((x,y))
	#방문 체크
	visited[x][y]=True

	#큐가 존재할때까지
	while q:
		#큐 값 pop
		x,y=q.popleft()
		#상하좌우 체크
		for i in range(4):
			nx = x+dx[i]
			ny = y+dy[i]
			if 0<=nx<N and 0<=ny<M:
				if paint[nx][ny]==1 and visited[nx][ny]==False:
					size+=1
					visited[nx][ny]=True
					q.append((nx,ny))
	return size

cnt=0
#하한값을 위한 wide=0
wide=0
for i in range(N):
	for j in range(M):
		if paint[i][j]==1 and visited[i][j]==False:
			cnt+=1
			#그림이 없는 경우를 대비해 max함수로 하한값 0으로 설정
			wide=max(wide,bfs(i,j)) #현재 위치 paint[i][j]가 1인거

print(cnt)
print(wide)

###########################################

# # 상하좌우 델타값
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
#
#
# # 넓이 구하는 함수
# def DFS(start_x, start_y):
#     area = 1
#     stack = [(start_x, start_y)]
#     while stack:
#         x, y = stack.pop()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0 <= nx < n and 0 <= ny < m:
#                 # paper 값이 1이고 방문하지 않았다면
#                 if paper[nx][ny] == 1 and not visited[nx][ny]:
#                     # 방문 표시
#                     visited[nx][ny] = 1
#                     # 넓이 추가
#                     area += 1
#                     stack.append((nx, ny))
#     return area
#
#
# n, m = map(int, input().split())
# paper = [list(map(int, input().split())) for _ in range(n)]
#
# visited = [[0] * m for _ in range(n)]
# max_area = 0
# cnt_painting = 0
#
# # 처음부터 끝까지 돌면서
# for i in range(n):
#     for j in range(m):
#         # paper 값이 1이고 방문한 적이 없으면
#         if paper[i][j] == 1 and not visited[i][j]:
#             # 방문 표시
#             visited[i][j] = 1
#             # 그림 개수 추가
#             cnt_painting += 1
#             # 넓이 최대값 구하기
#             max_area = max(max_area, DFS(i, j))
#
# print(cnt_painting)
# print(max_area)
#

##########################################################

# import sys
# input = sys.stdin.readline
#
# n, m = map(int, input().split())
# paint = [list(map(int, input().split())) for _ in range(n)]
#
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
#
# def bfs(x, y):
#     w = 1
#     que = [(x, y)]
#     while que:
#         x, y = que.pop()
#         for i in range(4):
#             nx, ny = x+dx[i], y+dy[i]
#             if 0 <= nx < n and 0 <= ny < m:
#                 if paint[nx][ny] == 1 and not check[nx][ny]:
#                     w += 1
#                     check[nx][ny] = 1
#                     que.append((nx, ny))
#     return w
#
# cnt, wide = 0, 0
# check = [[0]*m for _ in range(n)]
# for i in range(n):
#     for j in range(m):
#         if paint[i][j] == 1 and not check[i][j]:
#             cnt += 1
#             check[i][j] = 1
#             wide = max(wide, bfs(i, j))
# print(cnt)
# print(wide)
