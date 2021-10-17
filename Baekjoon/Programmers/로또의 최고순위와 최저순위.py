# def solution(lottos, win_nums):
#     counter = 0
#     answer = []
#     dic = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6}
#     for lotto in lottos:
#         if win_nums.count(lotto) > 0:
#             counter += 1
#     answer.append(dic[counter + lottos.count(0)])
#     answer.append(dic[counter])
#     return answer
#
#
# print(solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]));


from collections import Counter


def cal_prize(collect_num):

    if collect_num == 2:
        return 5
    elif collect_num == 3:
        return 4
    elif collect_num == 4:
        return 3
    elif collect_num == 5:
        return 2
    elif collect_num == 6:
        return 1

    return 6


def solution(lottos, win_nums):
    low, high = 0, 0

    for my_num in lottos:
        for win_num in win_nums:
            if my_num == win_num:
                low += 1

    high = low + Counter(lottos)[0]

    return [cal_prize(high), cal_prize(low)]

print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]));
