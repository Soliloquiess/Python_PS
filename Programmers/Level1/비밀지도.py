def solution(n, arr1, arr2):
    answer = []

    for i, j in zip(arr1, arr2):
        value = str(bin(i|j)[2:])        # 2:(2부터 하는 이유?= tmp결과 ex) '0b1101' )
        value = value.zfill(n)
        value = value.replace('1', '#')
        value = value.replace('0', ' ')
        answer.append(value)

    return answer

print(solution(5,[9, 20, 28, 18, 11],[30, 1, 21, 17, 28]))


# def solution(n, arr1, arr2):
#     answer = []
#
#     for i in range(n):
#         tmp = bin(arr1[i] | arr2[i])
#         # tmp결과 ex) '0b1101'
#         tmp = tmp[2:].zfill(n)
#         # tmp결과 ex) '01101'
#         tmp = tmp.replace('1', '#').replace('0', ' ')
#         # tmp결과 ex) ' ## #'
#         answer.append(tmp)
#
#     return answer