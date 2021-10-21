def solution(s):
    s_list = list(s)

    for i in range(len(s_list)):
        if i % 2 == 0:
            s_list[i] = s_list[i].upper()
        elif i % 2 == 1:
            s_list[i] = s_list[i].lower()

    answer = "".join(s_list)
    return answer

print(solution("try hello world"))
