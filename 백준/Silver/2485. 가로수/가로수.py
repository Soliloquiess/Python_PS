import math

N = int(input())
positions = [int(input()) for _ in range(N)]

# 간격들을 계산합니다
intervals = [positions[i+1] - positions[i] for i in range(N-1)]

# 간격들의 GCD를 순차적으로 계산합니다
gcd_all = intervals[0]
for interval in intervals[1:]:
    gcd_all = math.gcd(gcd_all, interval)

# 각 간격을 GCD로 나누고 필요한 가로수의 수를 계산합니다
additional_trees = 0
for interval in intervals:
    num_trees_needed = (interval // gcd_all) - 1
    additional_trees += num_trees_needed

# additional_trees = sum((interval // gcd_all - 1) for interval in intervals)

print(additional_trees)
