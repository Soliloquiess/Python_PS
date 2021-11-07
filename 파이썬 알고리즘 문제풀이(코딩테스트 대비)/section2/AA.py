
def matrixsum(matrix, n):
    ans=0;

    for i in range(n):  # 0qn
        sum1 = sum2 = 0  # 행(ex)1행의 가로)의 합은 sum1 , 열(ex)1열의 세로)의 합은 sum2
        for j in range(n):
            sum1 += matrix[i][j]  # sum1엔 0행을 다 더해주는거
            sum2 += matrix[j][i]  # sum2엔 열을 다 더해주는거

        if (ans < sum1):
            ans = sum1;

        if (ans < sum2):
            ans = sum2;

    for k in range(n): #맨 위 0행 마지막열 까지(제일 긴 우상향 대각선)
        # traversing downwards starting
        # from first row
        row = 0
        col = k
        sum =0;

        while (col >= 0):
            print(matrix[row][col], end=" ")
            sum += matrix[row][col];
            row += 1
            col -= 1
            if(ans<sum):
                ans =sum;

    for j in range(1, n):#그 제일 긴 우상향 대각선이 끝나고 1행 n-1열부터 시작.(그대로 우상향)

        col = n - 1
        row = j
        # ans=0;
        sum =0;
        while (row < n):
            print(matrix[row][col], end=" ")

            sum += matrix[row][col];
            row += 1
            col -= 1
            if (ans < sum):
                ans = sum;

    for k in range(n): #맨 위 0행 마지막열 까지(제일 긴 우하향 대각선)

        row = 0
        col = k
        sum =0;

        while (col < n):
            print(matrix[row][col], end=" ")
            sum += matrix[row][col];
            row += 1
            col += 1
            if(ans<sum):
                ans =sum;


    for j in range(1, n):#그 제일 긴 우하향 대각선이 끝나고 1행 0열부터 시작(그대로 우햐항)

        col = 0
        row = j
        # ans=0;
        sum =0;
        while (row < n):
            print(matrix[row][col], end=" ")

            sum += matrix[row][col];
            row += 1
            col += 1
            if (ans < sum):
                ans = sum;


    return ans;

if __name__ == '__main__':
    n = 3
    # n=int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]

    print(matrixsum(matrix, n));




