A, B, C = map(int, input().split())

# 두 번째 줄 입력 받기
D = int(input())

current_seconds = A * 3600 + B * 60 + C

# 요리 시간을 더한 후의 총 초
total_seconds = current_seconds + D

# 새로운 시, 분, 초 계산
new_A = (total_seconds // 3600) % 24  # 시는 24로 나눈 나머지
total_seconds %= 3600
new_B = (total_seconds // 60) % 60   # 분은 60으로 나눈 나머지
new_C = total_seconds % 60           # 초는 60으로 나눈 나머지

# 결과 출력
print(new_A, new_B, new_C)