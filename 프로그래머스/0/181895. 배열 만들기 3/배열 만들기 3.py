def solution(arr, intervals):
    result = []
    for start, end in intervals:
        result += arr[start:end+1]
    return result
