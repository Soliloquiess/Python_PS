import sys

# sys.stdin = open("input.txt", "r")
board = [list(map(int, input().split())) for _ in range(7)]
# board라는 2차원 리스트에 읽음.
cnt = 0  # 개수세야
for i in range(3):  # 0,1,2,3,4,5,6까지인데 어차피 0,1,2넘는 3 이상 가면 5자가 안만들어져서 볼 필요가 없음

    # 중요!!!!!!!!!!!)꼭 포문을 먼저 쓴다고 세로가 아님!!!(포문 i가 먼저 쓰였지만 여기선 세로가 아닌 가로로 쓰였다.)
    # 중요!!!!!!!!!!!)꼭 포문을 먼저 쓴다고 세로가 아님!!!(포문 i가 먼저 쓰였지만 여기선 세로가 아닌 가로로 쓰였다.)
    # 중요!!!!!!!!!!!)꼭 포문을 먼저 쓴다고 세로가 아님!!!(포문 i가 먼저 쓰였지만 여기선 세로가 아닌 가로로 쓰였다.)

    for j in range(7):
        tmp = board[j][i:i + 5]  # j가 행, i가 슬라이스 기능해서 i+5까지. 맨첨은 0부터 4까지 돔
        if tmp == tmp[::-1]:  # 회문 판별
            cnt += 1
        # 여기까진 열(가로쪽으로만 탐색)

        # 여기부터는 행(세로)쪽도 봐야된다.
        # 가로쪽은 리스트라 슬라이스가 되는데 세로는 리스트가 아니라 슬라이스가 안 됨.
        # 그래서 밑으로 도는건 슬라이스 할 수밖에 없음.
        for k in range(2):
            if board[i + k][j] != board[i + 5 - k - 1][j]:
                # 열은 j(0~6까지 도는거(열은 가로))
                # 다르면 회문이 아님.
                # board[i + k][j] != board[i + 5 - k - 1][j]
                #
                break;
        else:  # 회문검사시 정상이면
            cnt += 1

print(cnt)

# # 회문의 길이가 가변적일 때 코드(이걸 강의에서 설명하심)
# import sys
#
# sys.stdin = open("input.txt", "r")
# board = [list(map(int, input().split())) for _ in range(7)]
# cnt = 0
# len = 5
# for i in range(3):  # 3개까지만 하는 이유는 4번째부터는 이미 5글자가 안되므로 고려 안함.
#     for j in range(7):
#         tmp = board[j][i:i + len]  # len -1 까지 도는거  (len이 5면 0,1,2,3,4)
#         if tmp == tmp[::-1]:  # 회문인지 확인 0이랑 tmp를 역순으로 하는거(거꾸로 만드는거) 이렇게 해서 두개가 같으면 회문이고
#             cnt += 1  # 카운트 한칸 늘려준다.
#         # tmp=board[i:i+5][j] 앞 행은 리스트가 아니라서 슬라이스가 안된다.
#         # 가로는 하나의 리스트라 슬라이스가 되는데 세로는 리스트가 안 되므로 슬라이스가 안 된다.
#         for k in range(len // 2):
#             if board[i + k][j] != board[len - k + i - 1][j]:
#                 # board[i + k][j] != board[len - k + i - 1][j] 이 부분이 다르면 회문이 아님.
#                 # board[i + k][j] != board[len - k + i - 1][j]
#
#                 break;
#         else:  # 정상 종료시 회문으로 cnt 1 증가시킴.
#             cnt += 1
#
# print(cnt)


#회문의 길이가 가변적일 때 코드(이걸 강의에서 설명하심)
# import sys
#
# sys.stdin = open("input.txt", "r")
# board = [list(map(int, input().split())) for _ in range(7)]
# cnt = 0
# len = 5
# for i in range(3):
#     for j in range(7):
#         tmp = board[j][i:i + len]
#         if tmp == tmp[::-1]:
#             cnt += 1
#         # tmp=board[i:i+5][j] 앞 행은 리스트가 아니라서 슬라이스가 안된다.
#         for k in range(len // 2):
#             if board[i + k][j] != board[len - k + i - 1][j]:
#                 break;
#         else:
#             cnt += 1
#
# print(cnt)