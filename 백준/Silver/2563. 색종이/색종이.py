# 도화지 크기
canvas_size = 100

# 도화지를 2차원 배열로 초기화 (0으로 초기화)
canvas = [[0] * canvas_size for _ in range(canvas_size)]

# 색종이의 수 입력
num_papers = int(input())

# 색종이 위치 입력 및 도화지에 색종이 붙이기
for _ in range(num_papers):
    x, y = map(int, input().split())
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            canvas[i][j] = 1

# 검은 영역의 넓이 계산
black_area = sum(sum(row) for row in canvas)

# 결과 출력
print(black_area)

#리스트 컴프리헨션 없이

# # 도화지 크기
# canvas_size = 100
#
# # 도화지를 2차원 배열로 초기화 (0으로 초기화)
# canvas = []
# for _ in range(canvas_size):
#     row = [0] * canvas_size
#     canvas.append(row)
#
# # 색종이의 수 입력
# num_papers = int(input())
#
# # 색종이 위치 입력 및 도화지에 색종이 붙이기
# for _ in range(num_papers):
#     x, y = map(int, input().split())
#     for i in range(x, x + 10):
#         for j in range(y, y + 10):
#             canvas[i][j] = 1
#
# # 검은 영역의 넓이 계산
# black_area = 0
# for row in canvas:
#     black_area += sum(row)
#
# # 결과 출력
# print(black_area)

