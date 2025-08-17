def solution(arr):
    n = len(arr)  # 배열 크기
    for i in range(n):
        for j in range(n):
            if arr[i][j] != arr[j][i]:  # 대칭이 아니면
                return 0
    return 1  # 모두 대칭이면
