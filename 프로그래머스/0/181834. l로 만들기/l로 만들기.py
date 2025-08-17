def solution(myString):
    answer = ''
    for c in myString:
        if c < 'l':        # 'l'보다 앞서는 문자면
            answer += 'l'  # 'l'로 바꿔서 추가
        else:
            answer += c    # 아니면 원래 문자 그대로 추가
    return answer
