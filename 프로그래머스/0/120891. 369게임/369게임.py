def solution(order):
    answer = 0
    for digit in str(order):
        if digit in '369':
            answer += 1
    return answer
