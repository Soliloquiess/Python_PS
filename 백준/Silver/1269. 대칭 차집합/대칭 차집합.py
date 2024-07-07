# 첫 번째 줄: 집합 A와 B의 원소 개수
n, m = map(int, input().split())

# 두 번째 줄: 집합 A의 원소들
A = set(map(int, input().split()))

# 세 번째 줄: 집합 B의 원소들
B = set(map(int, input().split()))

# 대칭 차집합 계산
symmetric_diff = A ^ B

# 대칭 차집합의 원소 개수 출력
print(len(symmetric_diff))
