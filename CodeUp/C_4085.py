m, n, x, y = map(int, input().split())

array = [[0]*m for _ in range(n)]

for i in range(n):
    num_list = list(map(int, input().split()))
    for j in range(m):
        array[i][j] = num_list[j]
    num_list = 0

flag = 0
sum = 0

for i in range(n-y+1):
    for j in range(m-x+1):
        for k in range(y):
            for l in range(x):
                sum += array[i+k][j+l]
        if (sum > flag):
            flag = sum
        sum = 0

print(flag)


#####
# m, n, x, y = list(map(int, input().split()))
#
# d = [[0 for j in range(m + 1)] for i in range(n + 1)]
#
# for i in range(n):
#     a = list(map(int, input().split()))
#     for j in range(m):
#         d[i + 1][j + 1] = a[j]
#
# ka = 0
# for i in range(y, n + 1):
#     for j in range(x, m + 1):
#         sum = 0
#
#         for ii in range(i - y + 1, i + 1):
#             for jj in range(j - x + 1, j + 1):
#                 sum += d[ii][jj]
#
#         if ka < sum:
#             ka = sum
#
# print(ka)