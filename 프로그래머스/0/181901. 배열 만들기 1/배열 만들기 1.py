def solution(n, k):
    answer =  [i for i in range(k, n + 1, k)]
    return answer


# def solution(n, k):
#     answer = []
#     i = k
#     while i <= n:
#         answer.append(i)
#         i += k
#     return answer