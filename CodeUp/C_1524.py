array = [[0]*11 for _ in range(11)]

for i in range(1, 10):
    num_list = list(map(int, input().split()))
    for j in range(1, 10):
        array[i][j] = num_list[j-1]
    num_list = 0

r, c = map(int, input().split())

i_list = [-1, -1, -1, 0, 0, 1, 1, 1]
j_list = [-1, 0, 1, -1, 1, -1, 0, 1]


def cal(i, j):
    cnt = 0
    for k in range(8):
        if (array[i+i_list[k]][j+j_list[k]] == 1):
            cnt += 1
    return cnt


if (array[r][c] != 1):
    print(cal(r, c))
elif (array[r][c] == 1):
    print(-1)




#######
# N = 9
# d = [[0 for j in range(N+2)] for i in range(N+2)]
#
# for i in range(N) :
#   a = list(map(int, input().split()))
#   for j in range(N) :
#     d[i+1][j+1] = a[j]
#
# r, c = input().split()
# r = int(r)
# c = int(c)
#
# dy = [-1, -1, -1, 0, 0, 1, 1, 1]
# dx = [-1, 0, 1, -1, 1, -1, 0, 1]
#
# answer = 0
# if d[r][c] == 1 :
#   answer = -1
# else :
#   check = 0
#   for i in range(8) :
#     check += d[r+dy[i]][c+dx[i]]
#   answer = check
#
# print(answer)


####

# matrix = [[0]*11 for i in range(11)]
#
# for i in range(1, 10):
#     input_list = list(map(int, input().split()))
#     for j in range(0, 9):
#         matrix[i][j+1] = input_list[j]
# r, c = map(int, input().split())
#
# if matrix[r][c] == 1:
#     print('-1')
# else:
#     mine = matrix[r-1][c-1] + matrix[r-1][c] + matrix[r-1][c+1] + \
#         matrix[r][c-1] + matrix[r][c+1] + matrix[r+1][c-1] + \
#         matrix[r+1][c] + matrix[r+1][c+1]
#     print(mine)
