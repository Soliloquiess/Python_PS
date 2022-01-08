def solution(arr):
    answer = []

    minVal = min(arr)
    arr.remove(minVal)

    if not arr:
        arr.insert(0, -1)

    return arr
print(solution([6,8,234,4,3,2,1]))
#딱히 정렬하라던가 이런 조건은 없었다.

# def solution(arr):
#     answer = []
#
#     if len(arr) == 1:
#         answer = [-1]
#     else:
#         minNum = min(arr)
#
#         answer = [num for num in arr if num != minNum]
#
#     return answer
#
# def solution(arr):
#     arr.pop(arr.index(min(arr)))
#     return arr if arr else [-1]