n, m, v = map(int, input().split())
s = [[0] * (n + 1) for _ in range(n + 1)]
visit = [0] * (n + 1)
for i in range(m):
    a, b = map(int, input().split())
    s[a][b] = 1
    s[b][a] = 1


def dfs(v):
    print(v, end=' ')
    visit[v] = 1
    for i in range(1, n + 1):
        if visit[i] == 0 and s[v][i] == 1:
            dfs(i)


def bfs(v):
    queue = [v]
    visit[v] = 0  # v는 탐색되었다.
    while (queue):
        v = queue[0]
        print(v, end=' ')
        del queue[0]
        for i in range(1, n + 1):
            if visit[i] == 1 and s[v][i] == 1:
                queue.append(i)
                visit[i] = 0  # i도 탐색완료


dfs(v)
print()
bfs(v)
#https://iwannabeadopedeveloper.tistory.com/336
# from collections import deque
# N, M, V = map(int, input().split())
# graph = [[0] * (N + 1) for _ in range(N + 1)]
#
# for _ in range(M):
#   m1, m2 = map(int, input().split())
#   # 노드 연결 하기
#   graph[m1][m2] = graph[m2][m1] = 1
#
# # 너비 우선 탐색
# def bfs(start_v):
#   discoverd = [start_v]
#   # 리스트를 써서 pop(0)하게 되면 시간복잡도가 O(N)이다.
#   # 그래서 시간복잡도가 O(1)인 deque를 사용한다.
#   queue = deque()
#   queue.append(start_v)
#
#   while queue:
#     v = queue.popleft()
#     print(v, end=' ')
#
#     for w in range(len(graph[start_v])):
#       if graph[v][w] == 1 and (w not in discoverd):
#         discoverd.append(w)
#         queue.append(w)
#
# # 깊이 우선 탐색
# def dfs(start_v, discoverd=[]):
#   discoverd.append(start_v)
#   print(start_v, end=' ')
#
#   for w in range(len(graph[start_v])):
#     if graph[start_v][w] == 1 and (w not in discoverd):
#       dfs(w, discoverd)
#
# dfs(V)
# print()
# bfs(V)