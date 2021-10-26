import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

K = int(input()) # test 수

def dfs(v):
    global result
    visited[v] = 1 # 방문한 정점 기록
    traced.append(v) # 탐색 경로 저장

    w = graph[v] # 다음 방문할 정점
    if visited[w] == 1: # 방문 가능한 곳이 끝났는지 체크
        if w in traced: # 탐색 경로에 다음 방문할 정점이 존재하면 순환
            result += traced[traced.index(w):] # 사이클이 되는 구간부터만 팀을 이룸
        return
    else:
        dfs(w) # 탐색 진행

for _ in range(K):
    V = int(input()) # 학생 수
    graph = [0] + list(map(int, input().split())) # 그래프 생성, 맨 앞에 [0]을 추가해 인덱스에 접근하기 편리하도록.
    visited = [0] * (V+1) # 방문한 정점를 담을 stack 생성
    result = [] # 팀을 구성한 학생 수

    for i in range(1, V+1): # 1번 학생부터 탐색 시작.
        if visited[i] == 0: # 방문한 정점이 아닌 경우에만 탐색 진행
            traced = [] # 탐색 경로 정보를 담을 stack 생성
            dfs(i)

    print(V - len(result))

# from collections import deque
#
# for _ in range(int(input())):
#     n = int(input())
#     arr = [0]
#     arr.extend(list(map(int, input().split())))
#     students = [[] for _ in range(n+1)]
#     # 진입차수 표시 위한 리스트
#     indegree = [0] * (n+1)
#
#     for a, b in enumerate(arr):
#         if a != 0:
#             students[a].append(b)
#
#     for i in arr:
#         if i > 0:
#             indegree[i] += 1
#
#     que = deque()
#     # 사이클이 존재하지 않는 정점 모으는 리스트
#     no_cycle = []
#
#     for i in range(1, n+1):
#         if indegree[i] == 0:
#             que.append(i)
#
# 	# 진입차수가 없고, 사이클이 없는 정점 no_cycle에 추가
#     while que:
#         now = que.popleft()
#         no_cycle.append(now)
#
#         for i in students[now]:
#             indegree[i] -= 1
#             if indegree[i] == 0:
#                 que.append(i)
#
#     print(len(no_cycle))
#   https://dapsu-startup.tistory.com/entry/%EB%B0%B1%EC%A4%80BAEKJOON-%ED%85%80-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-9466-%ED%8C%8C%EC%9D%B4%EC%8D%ACPython