n, m = map(int, input().split())
arr = [[0] * m for _ in range(n)]

cnt = 0
for k in range(n + m):
    for i in range(m):
        for j in range(n):
            if i + j == k:
                cnt += 1
                arr[j][i] = cnt

for i in arr:
    print(*i, ' ')

# https://ywtechit.tistory.com/90?category=930541