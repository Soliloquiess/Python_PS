def solution(my_string):
    answer = ""
    for c in my_string:
        if c == "a":
            answer += c.upper()
        elif c == "A":  
            answer += "A"  # "A"는 그대로 유지 (추가된 조건)
        elif c == c.upper():
            answer += c.lower()
        else:   
            answer += c  # 기존 소문자는 그대로 둠
    return answer
