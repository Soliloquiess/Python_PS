def solution(my_string, alp):
    result = ""
    for c in my_string:
        if c == alp:
            result += c.upper()
        else:
            result += c
    return result


#def solution(my_string, alp):
#    answer = my_string.replace(alp, alp.upper())
#    return answer