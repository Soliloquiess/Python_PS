def open_windows_count(N):
    # 직접 제곱근을 구하는 이분 탐색 알고리즘
    left, right = 0, N
    while left <= right:
        mid = (left + right) // 2
        if mid * mid == N:
            return mid
        elif mid * mid < N:
            left = mid + 1
        else:
            right = mid - 1
    return right

N = int(input())
print(open_windows_count(N))  