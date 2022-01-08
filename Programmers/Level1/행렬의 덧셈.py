def solution(arr1, arr2):
    for i in range(len(arr1)):
        for j in range(len(arr1[i])):  # for j in range(len(arr1[0])): 이렇게 arr1[0]이렇게 써도 똑같은 문장
            arr1[i][j] += arr2[i][j]
    return arr1

print(solution([[1, 2], [2, 3]], [[3, 4], [5, 6]]))