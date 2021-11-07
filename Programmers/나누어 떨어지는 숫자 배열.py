def solution(arr, divisor):
    answer = []
    for i in range(len(arr)) :
        if arr[i] % divisor == 0 :
            answer.append(arr[i])
    if len(answer) == 0 :
        answer.append(-1)
    else :
        answer.sort()
    return answer

print(solution([5, 9, 7, 10],5))
print(solution([2, 36, 1, 3],1))