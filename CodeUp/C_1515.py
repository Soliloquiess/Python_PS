array = [[0]*27 for _ in range(27)]
result = [[0]*27 for _ in range(27)]

for i in range(25):
    num_list = list(map(int, input().split()))
    for j in range(25):
        array[i][j] = num_list[j]
    num_list = []

j_list = [-1, -1, -1, 0, 1, 1, 1, 0]    #dy
i_list = [-1, 0, 1, 1, 1, 0, -1, -1]    #dx
#좌상부터 시계방향 탐색
#https://machine-geon.tistory.com/112(이 8방 탐색은 이 블로그 참조)


def life(i, j):
    zero_life = 0

    for k in range(8):
        if(array[i_list[k]+i][j_list[k]+j] == 1):
            zero_life += 1
    return zero_life


for i in range(25):
    for j in range(25):
        cnt = life(i, j)
        if(array[i][j] == 0):
            if(cnt == 3):
                result[i][j] = 1
            else:
                result[i][j] = 0
        elif(array[i][j] == 1):
            if(4 <= cnt or cnt <= 1):
                result[i][j] = 0
            elif(cnt == 2 or cnt == 3):
                result[i][j] = 1
            else:
                result[i][j] = 0

for i in range(25):
    for j in range(25):
        print(result[i][j], end=' ')
    print('')




# matrix = [[0]*27 for i in range(27)]
# next_generation = [[0]*27 for i in range(27)]
#
# for i in range(1, 26):
#     input_list = list(map(int, input().split()))
#     for j in range(0, 25):
#         matrix[i][j+1] = input_list[j]
#
# for i in range(1, 26):
#     for j in range(1, 26):
#         life = matrix[i-1][j-1] + matrix[i][j-1] + matrix[i+1][j-1] + \
#             matrix[i-1][j] + matrix[i+1][j] + matrix[i-1][j+1] + \
#             matrix[i][j+1] + matrix[i+1][j+1]
#         if matrix[i][j] == 0:
#             next_generation[i][j] = 1 if life == 3 else 0
#         else:
#             next_generation[i][j] = 1 if life == 2 or life == 3 else 0
#
# for i in range(1, 26):
#     for j in range(1, 26):
#         print(next_generation[i][j], end=' ')
#     print()