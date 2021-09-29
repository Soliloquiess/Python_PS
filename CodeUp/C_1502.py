n = int(input());

Arr = [[0] * n for _ in range(n)];
x = 0;
for i in range(n):
    for j in range(n):
        x += 1;
        Arr[j][i] = x;

for i in range(0, n):
    for j in range(0, n):
        print(Arr[i][j], end=" ")
    print("")

# n = int(input())
# array = [[0]*n for _ in range(n)]
# flag = 1
#
# for j in range(n):
#     for i in range(n):
#         array[i][j] = flag
#         flag += 1
#
# for i in range(n):
#     for j in range(n):
#         print(array[i][j], end=' ')
#     print(' ')