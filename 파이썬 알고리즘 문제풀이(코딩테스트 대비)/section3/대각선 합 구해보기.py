# Python 3 program to print matrix downward

def printMatrixDiagonallyDown(matrix, n):
    # printing elements above and on
    # second diagonal
    for k in range(n):
        # traversing downwards starting
        # from first row
        row = 0
        col = k
        while (col >= 0):
            print(matrix[row][col], end=" ")
            row += 1
            col -= 1

    # printing elements below second
    # diagonal
    for j in range(1, n):
        # traversing downwards starting
        # from last column
        col = n - 1
        row = j
        while (row < n):
            print(matrix[row][col], end=" ")
            row += 1
            col -= 1


if __name__ == '__main__':
    n = 3
    matrix = [list(map(int, input().split())) for _ in range(n)]

    printMatrixDiagonallyDown(matrix, n)

# This code is contributed by Surendra_Gangwar
#https://www.geeksforgeeks.org/print-the-matrix-diagonally-downwards/