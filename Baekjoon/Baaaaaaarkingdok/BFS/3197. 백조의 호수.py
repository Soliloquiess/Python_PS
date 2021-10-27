from collections import deque
import sys

input = sys.stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs():
    while q:
        x, y = q.popleft()
        if x == x2 and y == y2:
            return 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if not c[nx][ny]:
                    if a[nx][ny] == '.':
                        q.append([nx, ny])
                    else:
                        q_temp.append([nx, ny])
                    c[nx][ny] = 1
    return 0

def melt():
    while wq:
        x, y = wq.popleft()
        if a[x][y] == 'X':
            a[x][y] = '.'
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if not wc[nx][ny]:
                    if a[nx][ny] == 'X':
                        wq_temp.append([nx, ny])
                    else:
                        wq.append([nx, ny])
                    wc[nx][ny] = 1

m, n = map(int, input().split())
c = [[0]*n for _ in range(m)]
wc = [[0]*n for _ in range(m)]

a, swan = [], []
q, q_temp, wq, wq_temp = deque(), deque(), deque(), deque()

for i in range(m):
    row = list(input().strip())
    a.append(row)
    for j, k in enumerate(row):
        if a[i][j] == 'L':
            swan.extend([i, j])
            wq.append([i, j])
        elif a[i][j] == '.':
            wc[i][j] = 1
            wq.append([i, j])

x1, y1, x2, y2 = swan
q.append([x1, y1])
a[x1][y1], a[x2][y2], c[x1][y1] = '.', '.', 1
cnt = 0

while True:
    melt()
    if bfs():
        print(cnt)
        break
    q, wq = q_temp, wq_temp
    q_temp, wq_temp = deque(), deque()
    cnt += 1


#문제는 어렵지 않은데 시간 초과를 해결하는 것이 쉽지 않았다. 아래와 같이 풀면 된다

# 물bfs -> 빙판 칸 물임시큐 저장 -> 백조bfs -> 빙판 칸 백조임시큐 저장 -> 물, 백조 큐를 임시큐로 바꾼다 -> 반복
#
# 맨 처음에 백조에 해당하는 칸도 물에 대한 큐에 넣어줘야 하는것을 주의해야한다

#1. 백조, 물을 각각 저장할 큐와 다음 위치를 저장할 임시 큐 2개씩 총 4개의 큐를 만든다
#2. 얼음이 녹는 것을 물이 이동하는 것으로 처리한다. 물에 대한 bfs를 먼저 실행
# 3. 다음 칸이 빙판이면 다음번 bfs 때 물이 되기 때문에 바로 녹이지 않고 임시큐에 넣는다
# 4. 현재 상황에서 백조가 이동할 수 있는만큼 이동한다. 다음 칸이 빙판이면 임시큐에 넣는다
# 5. 백조가 만나지 못하면 물과 백조에 대한 큐를 각각의 임시큐로 치환하고 임시큐를 초기화한다
# 6. 만날 때까지 과정 반복
#





import sys
from collections import deque

maps = []
birds = []
r, c = map(int, sys.stdin.readline().split())
for y in range(r):
    arr = list(sys.stdin.readline().replace("\n", ""))
    maps.append(arr)
    for x in range(len(arr)):
        if arr[x] == "L":
            birds.append((y, x))

# 해당위치는 몇 초 후에 전부 녹는지를 저장한 배열
time = [[0 for _ in range(c)] for _ in range(r)]


# 빙하가 녹는 시간대를 time에 저장하고
# 가장 마지막으로 빙하가 녹은 시간이 몇 초인지를 리턴하는 함수
def melt_time_set(maps: list) -> int:
    visited = [[False for _ in range(c)] for _ in range(r)]
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    # 처음에 바다이거나 백조인 부분
    queue = deque()
    for y in range(len(maps)):
        for x in range(len(maps[0])):
            if maps[y][x] == '.' or maps[y][x] == 'L':
                queue.append((y, x))
                time[y][x] = 0
                visited[y][x] = True

    # 마지막으로 빙하가 녹은 시간
    last_time = 0
    # 각 위치의 빙하가 녹는 데 몇 초가 필요한지
    while queue:
        y, x = queue.popleft()
        for dy, dx in dirs:
            ny, nx = y + dy, x + dx
            if 0 <= ny < len(maps) and 0 <= nx < len(maps[0]) and not visited[ny][nx] and maps[ny][nx] != "L":
                queue.append((ny, nx))
                time[ny][nx] = time[y][x] + 1
                visited[ny][nx] = True
                last_time = time[ny][nx]
    return last_time


# bfs(백조1 위치, 빙하, 이분탐색 기준값, 백조2 위치)
def bfs(start: tuple, maps: list, mid: int, end: tuple) -> bool:
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    queue = deque()
    queue.append(start)
    visited = [[False for _ in range(len(maps[0]))] for _ in range(len(maps))]
    while queue:
        y, x = queue.popleft()
        visited[y][x] = True
        for dy, dx in dirs:
            ny, nx = y + dy, x + dx
            if 0 <= ny < len(maps) and 0 <= nx < len(maps[0]) and not visited[ny][nx]:
                visited[ny][nx] = True
                # 백조1이 백조2 위치에 도착할 수 있는 경우
                if ny == end[0] and nx == end[1]:
                    return True
                # 기준 시간초인 mid보다 작은 빙하는 녹아서 이동가능한 것으로 간주
                if time[ny][nx] <= mid:
                    queue.append((ny, nx))
    return False


_min, _max = 0, melt_time_set(maps)
answer = _max
while _min <= _max:
    mid = (_min + _max) // 2
    if bfs(birds[0], maps, mid, birds[1]):
        answer = mid
        _max = mid - 1
    else:
        _min = mid + 1
print(answer)