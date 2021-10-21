T = int(input())
for test_case in range(T):
    C = input()
    N = int(input())
    arr = input().rstrip()[1:-1].split(",")

    if N == 0:
        arr = []

    l, r, re = 0, 0, True

    for com in C:
        if com == "R":
            re = not re
        else:
            if re is True:
                l += 1
            else:
                r += 1
    if r + l <= N:
        answer = arr[l:N - r]
        if re is True:
            print("[" + ",".join(answer) + "]")
        else:
            print("[" + ",".join(answer[::-1]) + "]")
    else:
        print("error")


#https://donghak-dev.tistory.com/26

# import sys
# from collections import deque
#
# TC = int(sys.stdin.readline())
#
# for _ in range(TC):
#     cmd = sys.stdin.readline().strip()
#     size = int(sys.stdin.readline())
#
#     # 덱에 입력받아서 넣기
#     line = sys.stdin.readline()[1:-2].split(",")
#     queue = deque()
#     for each in line:
#         if each != '':
#             queue.append(each)
#
#     errorflag = 0
#     reverse = 0
#
#     # 명령어 하나씩
#     for each in cmd:
#         if each == "R": # reverse(flag) 바꿔주기
#             if reverse == 0:
#                 reverse = 1
#             else:
#                 reverse = 0
#         else: #  D면 reverse(flag)방향에 따라 앞이나 뒤에서 하나씩 삭제
#             if queue and queue[0] != '':
#                 if reverse == 0:
#                     queue.popleft()
#                 else:
#                     queue.pop()
#             else:
#                 errorflag = 1
#                 break
#
#     if errorflag == 1:  # 에러플래그 1이면 에러 출력
#         print("error")
#     else:
#         if reverse == 1:  # 리버스 플래그 1이면 뒤집어서 출력
#             queue.reverse()
#
#         print("[", end='')
#         for i in range(len(queue)):
#             if i == len(queue)-1:
#                 print(str(queue[i]),end='')
#             else:
#                 print(queue[i],end=',')
#         print("]")