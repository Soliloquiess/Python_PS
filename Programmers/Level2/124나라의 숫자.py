def solution(n):
    answer = ''
    while n:
        if n % 3:   #n%3이 0이 아니면
            answer += str(n % 3)
            n //= 3
        else:
            answer += "4"
            n = n//3 - 1
    return answer[::-1] #맨 뒤에서부터 역순으로 출력
print(solution(6))