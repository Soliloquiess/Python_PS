def solution(str_list, ex):
    answer = ""
    for s in str_list:
        if ex not in s:   # 제외 문자열이 없으면 이어붙임
            answer += s
    return answer

#def solution(str_list, ex):
#    answer = ""
#   for s in str_list:
#        if s.find(ex) == -1:   # ex가 없으면 (-1은 없다는 의미)
#            answer += s
#    return answer
