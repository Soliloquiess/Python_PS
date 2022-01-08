def solution(left, right):
    answer = 0

    for i in range(left, right + 1):
        tmp = 0
        for j in range(1, i + 1):   #약수 개수 구하기.
            if i % j == 0:
                tmp += 1
        if tmp % 2 == 0:    #약수의 개수가 짝수면
            answer += i
        else:               #약수의 개수가 홀수면
            answer -= i

    return answer

print(solution(13,17))