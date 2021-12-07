import sys

# sys.stdin=open("input.txt", "r")
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def DFS(x, y):
    global cnt
    if x == ex and y == ey:
        cnt += 1
    else:
        for k in range(4):
            xx = x + dx[k]
            yy = y + dy[k]  # 현재 지점에서 시계방향으로 봄

            if 0 <= xx < n and 0 <= yy < n and ch[xx][yy] == 0 and board[xx][yy] > board[x][y]:
                # 0<=xx<n and 0<=yy<n and ch[xx][yy]==0 경계선 벗어나지 않게
                # board[xx][yy]>board[x][y]: 가려고 하는 지점이 현재 지점보다 커야지만 이동하는거

                ch[xx][yy] = 1  # 가려고 하는 지점
                DFS(xx, yy)  # dfs로 뻗어나감
                ch[xx][yy] = 0  # 백했을때(dfs로 위아래가 대칭 위에서 한 행동 취소할떄 체크 해제)
                # 위에서 한 행동을 풀어준다.
    return cnt;

if __name__ == "__main__":
    n = int(input())
    board = [[0] * n for _ in range(n)]  # 지도 정보
    ch = [[0] * n for _ in range(n)]  # 어떠한 경로 지나쳐왔는지 체크하는 체크리스트
    max = -2147000000
    min = 2147000000
    for i in range(n):
        tmp = list(map(int, input().split()))  # 여기서 한 줄을 읽음.(tmp에 들어갔다

        for j in range(n):  # j가 tmp를 접근해간다.(한 줄 읽은 것을 접근한다,)
            if tmp[j] < min:  # 한 줄에서 최소값이 발견 되면
                min = tmp[j]  # 그 떄 최소 값 교체
                sx = i  # sx,sy가 스타트 지점.
                sy = j  # 그 sx에 i가 행번호, 열 번호를 sy에 넣음
                # 즉 스타트 지점을 계속 갱신
                # 마지막은 출발지점 찾아냄

            if tmp[j] > max:  # 가장 높은지점 발견되면
                max = tmp[j]
                ex = i
                ey = j  # ex,ey는 도착지점의 행, 열 번호
                # 마지막엔 도착지점 찾아냄
            board[i][j] = tmp[j]  # 보드에 복사해 넣음.

    ch[sx][sy] = 1
    cnt = 0
    print(DFS(sx, sy))
    print(cnt)

# 앞 전 미로탐색과 비슷하지만 다른점이 출발점과 도착점이 입력에 따라 달라진다는 점이다.
# pdf의 문제의 경우 2->100으로 가는거 그리고 갈수록 수는 높아져야한다(산이므로)
# 산이기 떄문에 현재지점보다 앞으로 가야할 지점이 커야 길이 성립된다.

# 미로탐색과 아주 비슷하다.