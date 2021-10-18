def rank(arr):
    maxValue = max(arr)
    answer = []
    for i, v in enumerate(arr):
        if v >= maxValue:
            answer.append(i + 1)
    answer.sort()
    return answer


def solution(answers):
    answer = []
    collect = [0] * 3

    for i, ans in enumerate(answers):
        # 1번 수포자
        # 1 2 3 4 5 ...
        a1 = i % 5 + 1
        if ans == a1:
            collect[0] += 1

        # 2번 수포자
        # 2 1 / 2 3 / 2 4 / 2 5 ...
        mat2 = [2, 1, 2, 3, 2, 4, 2, 5]
        a2 = i % 8
        if ans == mat2[a2]:
            collect[1] += 1

        # 3번 수포자
        # 3 3 / 1 1 / 2 2 / 4 4 / 5 5 ...
        mat3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
        a3 = i % 10
        if ans == mat3[a3]:
            collect[2] += 1

    answer = rank(collect)
    return answer
print(solution([1, 2, 3, 4, 5]))
# https://latte-is-horse.tistory.com/100

# def solution(answers):
#     pattern1 = [1,2,3,4,5]
#     pattern2 = [2,1,2,3,2,4,2,5]
#     pattern3 = [3,3,1,1,2,2,4,4,5,5]
#     score = [0, 0, 0]
#     result = []
#
#     for idx, answer in enumerate(answers):
#         if answer == pattern1[idx%len(pattern1)]:
#             score[0] += 1
#         if answer == pattern2[idx%len(pattern2)]:
#             score[1] += 1
#         if answer == pattern3[idx%len(pattern3)]:
#             score[2] += 1
#
#     for idx, s in enumerate(score):
#         if s == max(score):
#             result.append(idx+1)
#
#     return result
