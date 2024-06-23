n = int(input())

# 수행 횟수 계산
if n < 3:
    count = 0
else:
    count = n * (n - 1) * (n - 2) // 6

print(count)
print(3)
