n = int(input());

Arr = [[0] * n for _ in range(n)];
x = 1;
for i in range(n):
    if(i%2==0):
        for j in range(n):
            Arr[j][i] = x;
            x += 1;
    else:
        for j in range(n-1, -1, -1):
            Arr[j][i] = x;
            x+=1;

for i in range(0, n):
    for j in range(0, n):
        print(Arr[i][j], end=" ")
    print("")

# n = int(input())
# array = [[0]*n for _ in range(n)]
# num = 1
#
# for j in range(n):
#     if (j % 2 == 0):
#         for i in range(n):
#             array[i][j] = num
#             num += 1
#     else:
#         for i in range(n-1, -1, -1):
#             array[i][j] = num
#             num += 1
#
# for i in range(n):
#     for j in range(n):
#         print(array[i][j], end=' ')
#     print(' ')