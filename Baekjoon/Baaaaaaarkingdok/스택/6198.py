import sys
n = int(input())
A = list(map(int, sys.stdin.readline().split()))
answer = [-1] * n
stack = []


stack.append(0)
for i in range(1, n):
    while stack and A[stack[-1]] < A[i]:
        answer[stack.pop()] = A[i]
    stack.append(i)


print(*answer)
#https://hongcoding.tistory.com/40


# 17298번 오큰수
# from collections import deque
#
# n = int(input())
# seq = list(map(int, input().split()))
#
# oh_big = [-1] * n
# stack = deque()
#
# for i in range(n):
#     while stack and (stack[-1][0] < seq[i]):
#         tmp, idx = stack.pop()
#         oh_big[idx] = seq[i]
#     stack.append([seq[i], i])
#
# print(*oh_big)
#https://hooongs.tistory.com/329
