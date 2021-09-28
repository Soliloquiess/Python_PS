n, m = map(int, input().split())
Arr = [[0]*m for _ in range(n)]

x=1;
i=n-1;
j=m-1;

Xaxis = -1;
Yaxis = -1;

for k in range(1,n*m+1):
    Arr[i][j] =x;
    x+=1;
    if (j <= m and Xaxis == 1 and Yaxis == 1):
        if (j+1 < m and Arr[i][j+1] == 0):
            j+=1;
        else:
            i+=1;
            Xaxis = -1;
    elif ( i <=n and Xaxis == -1 and Yaxis == 1):
        if (i+1 < n and Arr[i+1][j] == 0):
            i+=1;
        else:
            j-=1;
            Yaxis =-1;

    elif (j >=0 and Xaxis == -1 and Yaxis == -1):
        if (j-1 >= 0 and Arr[i][j-1] == 0):
            j-=1;
        else:
            i-=1;
            Xaxis = 1;

    elif (i >=0 and Yaxis == -1 and Xaxis == 1 ):
        if (i-1 >= 0 and Arr[i-1][j] == 0):
            i-=1;
        else:
            j+=1;
            Yaxis = 1;
for i in range(0,n):
    for j in range(0,m):
        print(Arr[i][j],end=" ");
    print("");
