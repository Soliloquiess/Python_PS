def solution(n):
    # 1. 빈 n x n 배열 생성
    #arr = [[0]*n for _ in range(n)]
    arr = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(0)
        arr.append(row)    


    # 2. 방향: 오른쪽, 아래, 왼쪽, 위
    dx = [0, 1, 0, -1]  # 행 이동
    dy = [1, 0, -1, 0]  # 열 이동
    
    x, y = 0, 0          # 시작 위치
    dir_idx = 0          # 방향 인덱스
    for num in range(1, n*n + 1):
        arr[x][y] = num
        
        # 다음 위치 계산
        nx, ny = x + dx[dir_idx], y + dy[dir_idx]
        
        # 범위를 벗어나거나 이미 숫자가 있으면 방향 전환
        if nx < 0 or nx >= n or ny < 0 or ny >= n or arr[nx][ny] != 0:
            dir_idx = (dir_idx + 1) % 4
            nx, ny = x + dx[dir_idx], y + dy[dir_idx]
        
        x, y = nx, ny
    
    return arr
