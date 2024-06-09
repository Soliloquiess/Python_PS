# 입력 받기
N = int(input())

# 첫째 줄부터 N번째 줄까지 출력
for i in range(1, N + 1):
    spaces = ' ' * (N - i)
    stars = '*' * (2 * i - 1)
    print(spaces + stars)

# N+1번째 줄부터 2N-1번째 줄까지 출력
for i in range(N - 1, 0, -1):
    spaces = ' ' * (N - i)
    stars = '*' * (2 * i - 1)
    print(spaces + stars)
