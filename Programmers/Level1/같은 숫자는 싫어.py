def solution(arr):
    b = []
    for i in range(len(arr)):
        if i == 0:
            b.append(arr[i])
        elif arr[i] != arr[i-1]:
            b.append(arr[i])

    return b

print(solution([1, 1, 3, 3, 0, 1, 1]))

# def solution(arr):
#     result = []
#     result.append(arr[0])
#     for i in range(1,len(arr)):
#         if arr[i] != arr[i-1]:
#             result.append(arr[i])
#     return result
# result 라는 list에서 첫 번째 리스트의 인덱스는 항상 arr의 인덱스 값을 가질 것이므로 초기값은 arr의 첫 번째 인덱스로 잡아줍니다. 그 이후 2번째 인덱스부터 arr 배열의 마지막 인덱스까지 전, 후 값을 비교하여 다르다면 이전 값을 append 해줍니다.