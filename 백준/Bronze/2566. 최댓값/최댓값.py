# 9x9 격자판 입력 받기
grid = []
for _ in range(9):
    row = list(map(int, input().split()))
    grid.append(row)

# 최댓값 및 위치 초기화
max_value = -1
max_row = -1
max_col = -1

# 격자판 순회하며 최댓값 찾기
for i in range(9):
    for j in range(9):
        if grid[i][j] > max_value:
            max_value = grid[i][j]
            max_row = i
            max_col = j

# 최댓값 출력
print(max_value)
# 최댓값의 위치 출력 (1-indexed)
print(max_row + 1, max_col + 1)
