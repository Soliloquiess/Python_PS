t = int(input())
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(x, y):
    queue = [[x, y]]
    while queue:
        a, b = queue[0][0], queue[0][1] # 현재 위치를 a, b에 넣어줘서 bfs 돈다.
        del queue[0]    #현재 들어간 위치 큐에서 제거
        for i in range(4):
            q = a + dx[i]
            w = b + dy[i]
            if 0 <= q < n and 0 <= w < m and s[q][w] == 1:  #범위가 사각 안이고 1인경우(배추인 경우)
                s[q][w] = 0
                queue.append([q, w])
for i in range(t):
    m, n, k = map(int, input().split())
    s = [[0] * m for i in range(n)]
    cnt = 0
    for j in range(k):
        a, b = map(int, input().split())
        s[b][a] = 1
    for q in range(n):
        for w in range(m):
            if s[q][w] == 1:
                bfs(q, w)
                s[q][w] = 0 #배추있던 부분을 0으로 바꿔준다.
                cnt += 1    #그리고 카운트 1개 추가
    print(cnt)