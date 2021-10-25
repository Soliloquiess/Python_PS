from collections import deque

M,N,K = map(int, input().split());
maps = [list(0 for _ in range(N)) for _ in range(M)];
for _ in range(K):
    left_x, left_y, right_x, right_y =  map(int, input().split());
    #일반적인 좌표는 왼쪽 위가 0,0에서 시작하니 이걸 바꿔줬다.

    for i in range(M-right_y, M-left_y):
        for j in range(left_x, right_x):
            maps[i][j] = 1; #직사각형을 색칠해준다.

dx = [-1,1,0,0];
dy = [0,0,1,-1];

def bfs(i,j):
    queue= deque([[i,j]])   #영역 시작 좌표를 queue에 넣어준다.
    maps[i][j] = 1 #다시 방문하지 않기 위해 1로 변경
    cnt = 1;
    while queue:
        now = queue.popleft();
        x,y = now[0], now[1];
        for i in range(4):
            nx = x+dx[i];
            ny = y+dy[i];
            if nx<0 or nx>M-1 or ny<0 or ny>N-1 :
                continue;

            if maps[nx][ny] ==0: #색칠되지 않은 곳만 계속 탐색
                queue.append([nx, ny]);
                maps[nx][ny]=1;
                cnt+=1;

    return cnt;


area = 0; #영역의 개수
cnts = [] #영역의 넓이

for i in range(M):
    for j in range(N):
        if maps[i][j] ==0: #영역이 시작되면
            cnts.append(bfs(i,j))
            area+=1;

print(area);
cnts.sort();
print(*cnts)

# # import sys
# # input = sys.stdin.readline
#
# def dfs(x, y):
#     stack = [(x, y)]
#     board[x][y] = True
#     num = 1
#
#     while stack:
#         x, y = stack.pop()
#         for dx, dy in zip(dxs, dys):
#             nx, ny = x + dx, y + dy
#             if nx < 0 or nx >= n or ny < 0 or ny >= m: continue
#             if not board[nx][ny]:
#                 stack.append((nx, ny))
#                 board[nx][ny] = True
#                 num += 1
#     ## 마지막에 영역의 크기를 리스트에 저장한다.
#     empty_list.append(num)
#
#
# if __name__ == '__main__':
#     n, m, k = map(int, input().split())
#     board = [[False] * m for _ in range(n)]
#
#     ## 직사각형이 존재하는 영역은 True로 변환
#     for _ in range(k):
#         y1, x1, y2, x2 = map(int, input().split())
#         for i in range(x1, x2):
#             for j in range(y1, y2):
#                 board[i][j] = True
#     ## 동 남 서 북
#     dxs = (0, 1, 0, -1)
#     dys = (1, 0, -1, 0)
#
#     empty_list = []
#     for i in range(n):
#         for j in range(m):
#             if not board[i][j]:  # False 라면
#                 dfs(i, j)  # 영역의 크기를 empty_list에 추가시키는 함수
#
#     print(len(empty_list))
#     print(' '.join(map(str, sorted(empty_list))))