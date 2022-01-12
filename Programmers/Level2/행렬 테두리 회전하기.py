def solution(rows, columns, queries):

    answer = []
    array = [[0 for col in range(columns)] for row in range(rows)]
    t = 1
    for row in range(rows):
        for col in range(columns):
            array[row][col] = t
            t += 1

    for x1,y1,x2,y2 in queries:
        tmp = array[x1-1][y1-1]
        mini = tmp

        for k in range(x1-1,x2-1):  ##왼쪽 세로
            test = array[k+1][y1-1]
            array[k][y1-1] = test
            mini = min(mini, test)

        for k in range(y1-1,y2-1):  # 하단 가로
            test = array[x2-1][k+1]
            array[x2-1][k] = test
            mini = min(mini, test)

        for k in range(x2-1,x1-1,-1):   # 왼쪽 세로
            test = array[k-1][y2-1]
            array[k][y2-1] = test
            mini = min(mini, test)

        for k in range(y2-1,y1-1,-1):   # 상단 가로
            test = array[x1-1][k-1]
            array[x1-1][k] = test
            mini = min(mini, test)

        array[x1-1][y1] = tmp
        answer.append(mini)

    return answer

print(solution(6,6,[[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]))

print(solution(3,3,[[1, 1, 2, 2], [1, 2, 2, 3], [2, 1, 3, 2], [2, 2, 3, 3]]))

print(solution(100,97,[[1, 1, 100, 97]]));