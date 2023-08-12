n, m, k = map(int, input().split())

d = [[0] * (m+1) for _ in range(n+1)]

for i in range(k):
    x1, y1, x2, y2, u = map(int, input().split())
    d[x1][y1] += u
    d[x2+1][y2+1] += u
    d[x2+1][y1] -= u
    d[x1][y2+1] -= u

for i in range(1, n+1):
    for j in range(1, m+1):
        d[i][j] += d[i-1][j] + d[i][j-1] - d[i-1][j-1]

for i in range(1, n+1):
    for j in range(1, m+1):
        print(d[i][j], end=' ')
    print()
