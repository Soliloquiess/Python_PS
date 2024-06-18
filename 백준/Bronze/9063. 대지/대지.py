# 입력 받기
N = int(input())
points = [tuple(map(int, input().split())) for _ in range(N)]

# x와 y의 최솟값과 최댓값 찾기
min_x = min(point[0] for point in points)
max_x = max(point[0] for point in points)
min_y = min(point[1] for point in points)
max_y = max(point[1] for point in points)

# 직사각형의 넓이 계산
width = max_x - min_x
height = max_y - min_y
area = width * height

# 출력
print(area)
#
# # 입력 받기
# N = int(input())
#
# # 초기값 설정
# first_x, first_y = map(int, input().split())
# min_x = max_x = first_x
# min_y = max_y = first_y
#
# # 나머지 점들 처리
# for _ in range(N - 1):
#     x, y = map(int, input().split())
#
#     if x < min_x:
#         min_x = x
#     if x > max_x:
#         max_x = x
#     if y < min_y:
#         min_y = y
#     if y > max_y:
#         max_y = y
#
# # 직사각형의 넓이 계산
# width = max_x - min_x
# height = max_y - min_y
# area = width * height
#
# # 출력
# print(area)
