def solution(m, n, board):
    answer = 0

    for i in range(len(board)):  # board 배열로 만들기
        popped = board.pop(0)
        board.append([p for p in popped])

    while True:  # 터진 블록이 없을 때까지 반복
        checked = []  # 이번 턴에 터져야 할 블록들 모음
        for i in range(m - 1):
            for j in range(n - 1):
                if board[i][j] == "0":  # 이미 블록이 터져 빈 자리면 패스
                    continue
                if board[i][j] == board[i][j + 1]:  # 연속으로 두 개가 동일한 블록이면, 밑에 두 개도 동일한지 확인
                    if board[i][j] == board[i + 1][j] and board[i][j + 1] == board[i + 1][j + 1]:
                        checked.append((i, j))
                        checked.append((i, j + 1))
                        checked.append((i + 1, j))
                        checked.append((i + 1, j + 1))  # 터져야 할 블록들 전부 저장

        if len(checked) == 0:  # 이번에 터진 블록이 없으면 종료
            break
        else:
            answer += len(set(checked))  # 모아둔 블록 다 터뜨리기!
            for c in checked:
                board[c[0]][c[1]] = '0'

            for c in reversed(checked):  # 블록들 내리기
                check_n = c[0] - 1
                put_n = c[0]

                while check_n >= 0:  # 터진 자리 위에 있는 블록들을 다 내린다.
                    if board[put_n][c[1]] == "0" and board[check_n][c[1]] != "0":
                        board[put_n][c[1]] = board[check_n][c[1]]
                        board[check_n][c[1]] = "0"
                        put_n -= 1

                    check_n -= 1

    return answer

#https://dev-note-97.tistory.com/105


# def solution(m, n, board):
#     answer = 0
#     for i in range(len(board)):
#         board[i] = list(board[i])
#
#     while True:
#         # 같은 모양의 2X2 블록을 찾으면 remove 배열에 1로 표시
#         remove = [[0]*n for _ in range(m)]
#         for i in range(m - 1):
#             for j in range(n - 1):
#                 if board[i][j] != 0 and board[i][j] == board[i][j + 1] and board[i][j] == board[i + 1][j] and board[i][j] == board[i + 1][j + 1]:
#                     remove[i][j], remove[i][j + 1], remove[i + 1][j], remove[i + 1][j + 1] = 1, 1, 1, 1
#         # 지워진 블록 개수 세기
#         count = 0
#         for i in range(m): count += sum(remove[i])
#         answer += count
#         # 지워진 블록이 없을 경우 break
#         if count == 0: break
#         # 지워진 블록을 위의 블록으로 채우기
#         for i in range(m - 1, -1, -1):
#             for j in range(n):
#                 if remove[i][j] == 1:
#                     x = i - 1
#                     while x >= 0 and remove[x][j] == 1: x -= 1
#                     if x < 0:
#                         board[i][j] = 0
#                     else:
#                         board[i][j] = board[x][j]
#                         remove[x][j] = 1
#
#     return answer

#https://mjmjmj98.tistory.com/125

print(solution(4,5,["CCBDE", "AAADE", "AAABF", "CCBBF"]		));