n  = int(input());


Arr=[[0] * n for _ in range(n)];
x=0;
for i in range(n):
    for j in range(n):
        x+=1;
        Arr[i][j] = x;
        print(Arr[i][j], end= " ");
    print("")

# n = int(input())
# flag = 1
#
# for i in range(n):
#     for j in range(n):
#         print(flag, end=' ')
#         flag += 1
#     print(' ')