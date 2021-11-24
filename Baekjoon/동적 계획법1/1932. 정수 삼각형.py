import sys

t = int(sys.stdin.readline())
n = [list(map(int, sys.stdin.readline().split())) for _ in range(0, t)]
dp = []
for i in range(1, t):
    for j in range(len(n[i])):
        if j == 0:
            n[i][j] += (n[i - 1][j])
        elif j == i:
            n[i][j] += (n[i - 1][j - 1])

        else:
            n[i][j] += (max(n[i - 1][j], n[i - 1][j - 1]))
print(max(n[t - 1]))

#https://pannchat.tistory.com/entry/%EB%B0%B1%EC%A4%80-1932-%EC%A0%95%EC%88%98%EC%82%BC%EA%B0%81%ED%98%95-%ED%8C%8C%EC%9D%B4%EC%8D%AC