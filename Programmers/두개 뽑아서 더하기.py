# def solution(numbers):
#     answer = []
#     for i in range(len(numbers)):
#         for j in range(i+1,len(numbers)):
#             if (numbers[j] + numbers[i]) not in answer:
#                 answer.append(numbers[j] + numbers[i])
#     return sorted(answer)
#
# print(solution([2,1,3,4,1]))

from itertools import combinations

def solution(numbers):
    answer = set()
    for i in list(combinations(numbers,2)):
        answer.add(sum(i))
    return sorted(answer)

print(solution([2,1,3,4,1]))