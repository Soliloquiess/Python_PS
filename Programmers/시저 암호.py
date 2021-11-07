def solution(s, n):
    answer = ''

    for c in s:
        if c == ' ':
            # 공백문자 처리
            answer += ' '
            continue
        scissor = ord(c) + n
        if (ord(c) in range(ord('A'), ord('Z') + 1) and scissor > ord('Z')) or \
                (ord(c) in range(ord('a'), ord('z') + 1) and scissor > ord('z')):
            # c가 대문자면서 n을 더했을 때 'Z'를 넘어가는 경우
            # c가 소문자면서 n을 더했을 때 'z'를 넘어가는 경우
            answer += chr(scissor - 26)
        else:
            # 'Z'나 'z'를 넘어가지 않는 경우
            answer += chr(scissor)  #다시 여기서 아스키 코드 숫자를 문자로 바꿔주자.

    return answer
print(solution("AB",1))
#https://latte-is-horse.tistory.com/135