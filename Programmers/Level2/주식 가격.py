#1. 브루트포스


# def solution(prices):
#     answer =[0] * len(prices)
#     for i in range(len(prices)):
#         for j in range(i+1, len(prices)):
#             if prices[i] <= prices[j]:
#                 answer[i]+=1
#             else:
#                 answer[i]+=1
#                 break
#     return answer

#2. 스택


# def solution(prices):
#     answer = [0] * len(prices)
#     stack = []
#
#     for i, price in enumerate(prices):
#         # stack이 비었이면 false
#         while stack and price < prices[stack[-1]]:
#             j = stack.pop()
#             answer[j] = i - j
#         stack.append(i)
#
#     # for문 다 돌고 Stack에 남아있는 값들 pop
#     while stack:
#         j = stack.pop()
#         answer[j] = len(prices) - 1 - j
#
#     return answer

# def solution(prices):
#     answer = [0] * len(prices)
#     stack = []
#     for time, item in enumerate(prices):
#         while stack and stack[-1][1] > item:
#             v = stack.pop()
#             answer[v[0]] = time - v[0]
#
#         stack.append([time, item])
#
#     # 끝까지 가격이 떨어지지 않은 애들
#     while stack:
#         time = stack.pop()[0]
#         answer[time] = len(prices) - 1 - time
#
#     return answer

#3. 큐
from collections import deque


def solution(prices):
    queue = deque(prices)
    answer = []

    while queue:
        price = queue.popleft()
        sec = 0
        for q in queue:
            sec += 1
            if price > q:
                break
        answer.append(sec)
    return answer

print(solution([1, 2, 3, 2, 3]));
