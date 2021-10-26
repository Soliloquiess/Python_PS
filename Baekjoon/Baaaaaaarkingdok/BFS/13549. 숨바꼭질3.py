import sys
from collections import deque

n, k = map(int, input().split())

q = deque()
vis = [-1] * 200001
q.append(n)
vis[n] = 0

while q:
    x = q.popleft()
    if x == k:
        print(vis[x])
        sys.exit()
    # 순간이동해서 갈수 있는곳을 구한다.
    if x * 2 <= 200000 and vis[x * 2] == -1:
        vis[x * 2] = vis[x]
        # appendleft를 통해 큐의 앞에 넣어 해당 초에 방문할 수 있도록 한다.
        q.appendleft(x * 2)
    # x-1 로 갈수 있는곳 1초 더한다.
    if x - 1 >= 0 and vis[x - 1] == -1:
        vis[x - 1] = vis[x] + 1
        q.append(x - 1)
    # x+1 로 갈 수 있는곳 1초 더한다.
    if x + 1 <= 200000 and vis[x + 1] == -1:
        vis[x + 1] = vis[x] + 1
        q.append(x + 1)
#   https://kyun2da.github.io/2020/09/21/hideandseek3/
# ###########
#
# from heapq import heappush, heappop
#
#
# def dijkstra(x):
#     q = []		# 다익스트라는 항상 동일하다! 힙이나 우선순위큐를 사용
#     heappush(q, (0, x))	# (가중치, 노드)의 형태로 삽입
#
#     field = [-1] * MAX	# 가중치(여기서는 걸린 시간) 행렬 초기화
#     field[x] = 0	# 시작 위치의 가중치는 항상 0
#
#     while q:
#         time, cx = heappop(q)
#         if cx == k:
#             return field[cx]
#
#         for i in range(3): # 이동할 수 있는 위치(X - 1, X + 1, X * 2) 세 개 고려
#             if i == 0:
#                 nx = cx - 1
#             elif i == 1:
#                 nx = cx + 1
#             else:
#                 nx = cx * 2
#
#             if not 0 <= nx < MAX:			   # 범위를 벗어나거나
#                 continue
#             if field[nx] != -1 and field[nx] <= field[cx]: # 이미 방문했고,
#                 continue				   # 지금까지 걸린 시간보다 적으면 갱신 안 함
#
#             if i < 2:			# 한 칸씩 이동한 경우 1초
#                 heappush(q, (time + 1, nx))
#                 field[nx] = time + 1
#             else:			# 순간이동한 경우 0초
#                 heappush(q, (time, nx))
#                 field[nx] = time
#
#
# n, k = map(int, input().split())
# MAX = 100001
# print(dijkstra(n))
#
#
# #######
#
#
# from collections import deque
#
#
# def bfs(x):
#     q = deque([x])		# 다익스트라와 달리 가중치(시간) 없음!
#     time = [-1] * MAX		# 중복방문을 위한 가중치행렬
#     time[x] = 0
#
#     while q:
#         cx = q.popleft()
#         if cx == k:
#             return time[cx]
#
#         for i in range(3):
#             if i == 0:
#                 nx = cx - 1
#             elif i == 1:
#                 nx = cx + 1
#             else:
#                 nx = cx * 2
#
#             if not 0 <= nx < MAX:	# 조건 검사 역시 다익스트라와 동일
#                 continue
#             if time[nx] != -1 and time[nx] <= time[cx]:
#                 continue
#
#             if i < 2:			# 한 칸씩 이동하는 경우 큐 뒤에 삽입
#                 q.append(nx)
#                 time[nx] = time[cx] + 1
#             else:			# 순간이동하는 경우 큐 앞에 삽입
#                 q.appendleft(nx)
#                 time[nx] = time[cx]
#
#
# n, k = map(int, input().split())
# MAX = 100001
# print(bfs(n))

#   https://summa-cum-laude.tistory.com/18