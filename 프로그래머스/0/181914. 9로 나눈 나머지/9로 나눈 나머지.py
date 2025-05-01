def solution(number):
    answer =  sum(int(digit) for digit in number )
    answer = answer % 9
    return answer