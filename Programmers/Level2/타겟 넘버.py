# def solution(numbers, target):
#     answer = 0
#     leaves = [0]
#     for num in numbers:
#         tmp = []
#         for parent in leaves:
#             tmp.append(parent + num)
#             tmp.append(parent - num)
#         leaves = tmp
#     for leaf in leaves:
#         if leaf == target:
#             answer += 1
#     return answer



# from collections import deque
# def solution(numbers, target):
#     answer = 0
#     queue = deque()
#     n = len(numbers)
#     queue.append([numbers[0],0])
#     queue.append([-1*numbers[0],0])
#     while queue:
#         temp, idx = queue.popleft()
#         idx += 1
#         if idx < n:
#             queue.append([temp+numbers[idx], idx])
#             queue.append([temp-numbers[idx], idx])
#         else:
#             if temp == target:
#                 answer += 1
#     return answer
#https://velog.io/@ju_h2/Python-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-level2-%ED%83%80%EA%B2%9F%EB%84%98%EB%B2%84-BFSDFS

# def solution(numbers, target):
#     n = len(numbers)
#     answer = 0
#     def dfs(idx, result):
#         if idx == n:
#             if result == target:
#                 nonlocal answer
#                 answer += 1
#             return
#         else:
#             dfs(idx+1, result+numbers[idx])
#             dfs(idx+1, result-numbers[idx])
#     dfs(0,0)
#     return answer

def solution(numbers, target):
    answer = DFS(numbers, target, 0)
    return answer

def DFS(numbers, target, depth):
    answer = 0
    if depth == len(numbers):
        print(numbers)
        if sum(numbers) == target:
            return 1
        else: return 0
    else:
        answer += DFS(numbers, target, depth+1)
        numbers[depth] *= -1
        answer += DFS(numbers, target, depth+1)
        return answer

print(solution([1, 1, 1, 1, 1],3))