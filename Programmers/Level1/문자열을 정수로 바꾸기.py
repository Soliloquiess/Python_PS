def solution(s):
    answer = 0
    operator = "+"

    if s[0] == "-":
        s = s[1:]
        answer = int(s) * -1
    elif s[0] == "+":
        s = s[1:]
        answer = int(s)
    else:
        answer = int(s)
    return answer

print(solution("1234"))