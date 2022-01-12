from collections import deque


def bfs(p):
    start = []

    for i in range(5):  # 시작점이 되는 P 좌표 구하기
        for j in range(5):
            if p[i][j] == 'P':
                start.append([i, j])

    for s in start:
        queue = deque([s])  # 큐에 초기값
        visited = [[0] * 5 for i in range(5)]  # 방문 처리 리스트
        distance = [[0] * 5 for i in range(5)]  # 경로 길이 리스트
        visited[s[0]][s[1]] = 1

        while queue:
            y, x = queue.popleft()

            dx = [-1, 1, 0, 0]  # 좌우
            dy = [0, 0, -1, 1]  # 상하

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < 5 and 0 <= ny < 5 and visited[ny][nx] == 0:

                    if p[ny][nx] == 'O':
                        queue.append([ny, nx])
                        visited[ny][nx] = 1
                        distance[ny][nx] = distance[y][x] + 1

                    if p[ny][nx] == 'P' and distance[y][x] <= 1:
                        return 0
    return 1


def solution(places):
    answer = []

    for i in places:
        answer.append(bfs(i))

    return answer


print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]));
#https://velog.io/@sem/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-LEVEL2-%EA%B1%B0%EB%A6%AC%EB%91%90%EA%B8%B0-%ED%99%95%EC%9D%B8%ED%95%98%EA%B8%B0-Python


# from collections import deque
#
# dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]  # 상하좌우
#
# def bfs(place, i, j):
#     visit = [[0]*5 for _ in range(5)]
#     q = deque()
#     q.append((i, j, 0))
#     visit[i][j] = 1
#
#     while q:
#         x, y, dist = q.popleft()
#         if 0 < dist < 3 and place[x][y] == 'P':
#             return False
#         if dist > 2:
#             break  # 거리가 3부터는 탐색 중단(거리두기를 잘 지킨 경우이기 때문에)
#         for k in range(4):
#             nx, ny, nd = x + dx[k], y + dy[k], dist + 1
#             if 0 <= nx < 5 and 0 <= ny <5:
#                 if place[nx][ny] != 'X' and not visit[nx][ny]:  # 파티션이 있는 경우만 아니면 이동가능
#                     q.append((nx, ny, nd))
#                     visit[nx][ny] = 1
#     return True
#
# def solution(places):
#     answer = []
#
#     for place in places:
#         chk = 0
#         for i in range(len(place)):
#             for j in range(len(place[0])):
#                 if place[i][j] == "P":
#                     if not bfs(place, i, j):
#                         answer.append(0)
#                         chk = 1
#                         break
#             if chk:
#                 break
#         else:
#             answer.append(1)
#     return answer

# print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]));
# https://whwl.tistory.com/199