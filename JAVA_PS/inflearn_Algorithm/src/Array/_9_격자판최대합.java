package Array;

import java.util.Scanner;


import java.util.*;
class _9_격자판최대합 {
    public int solution(int n, int[][] matrix) {
        int ans = -2147000000;
        int sum1 = 0, sum2 = 0;
        for (int i = 0; i < n; i++) {
            sum1 = sum2 = 0;
            for (int j = 0; j < n; j++) {
                sum1 += matrix[i][j];    //행이 고정 열이 도는거
                sum2 += matrix[j][i];    //행이 돌고 열이 고정되는거.
            }
            ans = Math.max(ans, sum1);
            ans = Math.max(ans, sum2);
        }
        sum1 = sum2 = 0;
        for (int i = 0; i < n; i++) {
            sum1 += matrix[i][i];    //우상향 대각선
            sum2 += matrix[i][n - i - 1];    //우하향 대각선
        }
        ans = Math.max(ans, sum1);
        ans = Math.max(ans, sum2);

        for (int k = 0; k < n; k++)//in range(n): //맨 위 0행 마지막열 까지(제일 긴 우상향 대각선)
//        # traversing downwards starting
//        # from first row 
        {
            int row = 0;
            int col = k;
            int sum = 0;

            while (col >= 0) {
//            # print(matrix[row][col], end=" ")
                sum += matrix[row][col];
                row += 1;
                col -= 1;
                if (ans < sum) {
                    ans = sum;
                }
            }
//        for j in range(1, n):#그 제일 긴 우상향 대각선이 끝나고 1행 n-1열부터 시작.(그대로 우상향)
            for (int j = 1; j < n; j++)//in range(n): //맨 위 0행 마지막열 까지(제일 긴 우상향 대각선)
            {
                col = n - 1;
                row = j;
//        # ans=0;
                sum = 0;
                while (row < n) {
//            # print(matrix[row][col], end=" ")

                    sum += matrix[row][col];
                    row += 1;
                    col -= 1;
                    if (ans < sum) {
                        ans = sum;
                    }
                }
//        for k in range(n): #맨 위 0행 마지막열 까지(제일 긴 우하향 대각선)
                for (k = 0; k < n; k++)//in range(n): //맨 위 0행 마지막열 까지(제일 긴 우상향 대각선)

                {
                    row = 0;

                    col = k;
                    sum = 0;

                    while (col < n) {
//            # print(matrix[row][col], end=" ")
                        sum += matrix[row][col];
                        row += 1;
                        col += 1;
                        if (ans < sum) {
                            ans = sum;
                        }
                    }
                }


//        for j in range(1, n)://그 제일 긴 우하향 대각선이 끝나고 1행 0열부터 시작(그대로 우햐항)
                for ( j = 1; j < n; j++)//in range(n): //맨 위 0행 마지막열 까지(제일 긴 우상향 대각선)
                {
                    col = 0;

                    row = j;
//        # ans=0;
                    sum = 0;
                    while (row < n) {
//             print(matrix[row][col], end=" ")
                        System.out.println(matrix[row][col] + " ");
                        sum += matrix[row][col];
                        row += 1;
                        col += 1;
                        if (ans < sum) {
                            ans = sum;

                        }
                    }
                }
            }
        }

        return ans;
    }

    public static void main(String[] args){
        _9_격자판최대합 T = new _9_격자판최대합();
        Scanner sc = new Scanner(System.in);
        int n=sc.nextInt();
        int[][] matrix=new int[n][n];
        for(int i=0; i<n; i++){
            for(int j=0; j<n; j++){
                matrix[i][j]=sc.nextInt();
            }
        }
        System.out.print(T.solution(n, matrix));
    }
}

/*

def solution(matrix, n):
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
            # print(matrix[row][col], end=" ")
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
            # print(matrix[row][col], end=" ")

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
            # print(matrix[row][col], end=" ")
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
            # print(matrix[row][col], end=" ")

            sum += matrix[row][col];
            row += 1
            col += 1
            if (ans < sum):
                ans = sum;


    return ans;

if __name__ == '__main__':
    # n = 3
    n=int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]

    print(solution(matrix, n));




# 5
# 1 0 0 0 0
# 100 2 0 0 0
# 0 101 3 0 0
# 0 0 102 4 0
# 0 0 0 103 5
#
#
# 4
# 10 5 9 6
# 8 15 3 2
# 3 8 12 3
# 2 11 7 3
#
# 3
# 71     12    45
# 114  5     6
# 7     8     9

 */