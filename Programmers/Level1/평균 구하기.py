def solution(arr):
    answer = 0
    answer = sum(arr) / len(arr)
    return answer

print(solution([1,2,3,4]))

# def average(list):
#     if len(list) == 0:
#         return 0
#     sum = 0
#     for i in list:
#         sum += i
#     return sum / len(list)

# list = [5,3,4]
# print("평균값 : {}".format(average(list)));