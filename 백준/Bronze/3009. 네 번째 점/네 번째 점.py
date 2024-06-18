# 세 점의 좌표 입력받기
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

# x 좌표와 y 좌표를 각각 리스트에 저장
x_coords = [x1, x2, x3]
y_coords = [y1, y2, y3]

# 한 번만 나타나는 x 좌표 찾기
if x_coords.count(x1) == 1:
    x4 = x1
elif x_coords.count(x2) == 1:
    x4 = x2
else:
    x4 = x3

# 한 번만 나타나는 y 좌표 찾기
if y_coords.count(y1) == 1:
    y4 = y1
elif y_coords.count(y2) == 1:
    y4 = y2
else:
    y4 = y3

# 네 번째 점의 좌표 출력
print(x4, y4)


# arrX = []
# arrY = []
# for i in range(3):
#         x, y = map(int, input().split())
#         arrX.append(x)
#         arrY.append(y)
# for i in range(3):
#         if arrX.count(arrX[i]) == 1:
#                 x = arrX[i]
#         if arrY.count(arrY[i]) == 1:
#                 y = arrY[i]
# print(x, y)
# https://pacific-ocean.tistory.com/131

# x_nums = []
# y_nums = []
# for _ in range(3):
#     x, y = map(int, input().split())
#     x_nums.append(x)
#     y_nums.append(y)
#
# for i in range(3):
#     if x_nums.count(x_nums[i]) == 1:
#         x4 = x_nums[i]
#     if y_nums.count(y_nums[i]) == 1:
#         y4 = y_nums[i]
# print(x4, y4)

# https://ooyoung.tistory.com/103