# 행렬 덧셈 프로그램

# 입력 받기
N, M = map(int, input().split())

# 행렬 A 입력 받기
A = []
for _ in range(N):
    row = list(map(int, input().split()))
    A.append(row)

# 행렬 B 입력 받기
B = []
for _ in range(N):
    row = list(map(int, input().split()))
    B.append(row)

# 행렬 C 구하기 (A와 B의 합)
C = []
for i in range(N):
    row = []
    for j in range(M):
        row.append(A[i][j] + B[i][j])
    C.append(row)

# 행렬 C 출력하기
for row in C:
    print(" ".join(map(str, row)))
