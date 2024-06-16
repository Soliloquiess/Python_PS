up, down, length = list(map(int,input().split()))

# 남은 거리 계산
remaining_distance = length - down

# 하루에 올라가는 속도
speed_per_day = up - down

# 일수 계산
days_needed = remaining_distance // speed_per_day
if remaining_distance % speed_per_day != 0:
    days_needed += 1

print(days_needed) 

# up, down, length = list(map(int,input().split()))
#
# day = (length-down)/(up-down);
#
# #나머지가 있을 경우(잔여 블록이 있을 경우)
#
# if((length-down)%(up-down)!=0):
#     day+=1;
# print(int(day))

################################################################### 
# # 입력 받기
# A, B, V = map(int, input().strip().split())
# 
# # 필요한 날 계산
# if A >= V:
#     days = 1
# else:
#     days = (V - A + (A - B) - 1) // (A - B) + 1
# 
# # 결과 출력
# print(days)


# import math
#
# a, b, v = map(int, input().split())
# # a= 올라가는 길이, b= 떨어지는길이, v= 나무높이
#
# day = math.ceil((v-a)/(a-b)) + 1
# print(day)
