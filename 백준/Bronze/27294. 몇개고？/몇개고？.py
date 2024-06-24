T, S = map(int, input().split())

# 조건에 따라 밥알 갯수를 결정합니다.
if 12 <= T <= 16 and S == 0:
    print(320)
else:
    print(280)
