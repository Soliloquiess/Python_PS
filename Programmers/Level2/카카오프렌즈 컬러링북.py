# from collections import deque
# m,n=map(int,input().split())
# visited = [[0 for _ in range(100)] for _ in range(100)]
# picture =[[1, 1, 1, 0], [1, 2, 2, 0], [1, 0, 0, 1], [0, 0, 0, 1], [0, 0, 0, 3], [0, 0, 0, 3]]
# dy = [1,-1,0,0]
# dx = [0,0,1,-1]
# def bfs(pixel,y,x):
#     cnt=0
#     q=deque()
#     q.append((y,x))
#     while q:
#         fy,fx=q.popleft()
#         for i in range(4):
#             gy,gx=fy+dy[i],fx+dx[i]
#             if 0<=gy<m and 0<=gx<n:
#                 if picture[gy][gx]==pixel and visited[gy][gx]!=1:
#                     cnt+=1
#                     visited[gy][gx]=1
#                     q.append((gy,gx))
#     return cnt
# def solution(m,n,picture):
#     number_of_area=0
#     max_size_of_one_area=0
#     take=[]
#     for i in range(m):
#         for j in range(n):
#             if visited[i][j]!=1 and picture[i][j]!=0:
#                 max_size_of_one_area=max(bfs(picture[i][j],i,j),max_size_of_one_area)
#                 number_of_area+=1
#     return number_of_area,max_size_of_one_area
# print(solution(m,n,picture))

#https://vixxcode.tistory.com/54


# https://programmers.co.kr/learn/courses/30/lessons/1829
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def solution(m, n, picture):
    answer = [0, 0]
    visited = [[False] * n for _ in range(m)]

    def bfs(x, y):
        count = 1
        # 큐(Queue) 구현을 위해 deque 라이브러리 사용
        queue = deque([(x, y)])
        # 현재 노드를 방문 처리
        visited[x][y] = True
        color = picture[x][y]
        # 큐가 빌 때까지 반복
        while queue:
            # 큐에서 하나의 원소를 뽑아 출력
            x, y = queue.popleft()
            # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if -1 < nx < m and -1 < ny < n:
                    if not visited[nx][ny] and picture[nx][ny] == color:
                        queue.append((nx, ny))
                        visited[nx][ny] = True
                        count += 1
        answer[0] += 1
        answer[1] = max(answer[1], count)

    for i in range(m):
        for j in range(n):
            if not visited[i][j] and picture[i][j] != 0:
                bfs(i, j)
    return answer


print(solution(6, 4, [[1, 1, 1, 0], [1, 2, 2, 0], [1, 0, 0, 1], [0, 0, 0, 1], [0, 0, 0, 3], [0, 0, 0, 3]]))
print(solution(6, 4, [[1, 1, 1, 0], [1, 1, 1, 0], [0, 0, 0, 1], [0, 0, 0, 1], [0, 0, 0, 1], [0, 0, 0, 1]]))