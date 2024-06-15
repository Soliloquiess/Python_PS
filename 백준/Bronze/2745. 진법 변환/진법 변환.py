# 입력을 받아 공백으로 분리합니다.
N, B = input().split()
# N은 진법 수, B는 진법입니다.
B = int(B)

# N을 B진법에서 10진법으로 변환합니다.
decimal_value = int(N, B)

# 변환된 값을 출력합니다.
print(decimal_value)
