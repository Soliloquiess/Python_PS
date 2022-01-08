def solution(num):
    answer = 0

    while True:
        if num == 1:
            break
        if answer > 499:
            answer = -1
            break

        if num % 2 == 0:
            num = num / 2
        elif num % 2 == 1:
            num = num * 3 + 1
        answer = answer + 1
    return answer

print(solution(1))