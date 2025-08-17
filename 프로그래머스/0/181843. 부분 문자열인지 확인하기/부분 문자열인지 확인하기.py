def solution(my_string, target):
    if target in my_string:   # 부분 문자열이면 True
        return 1
    else:
        return 0

#def solution(my_string, target):
#    if my_string.find(target) != -1:  # 부분 문자열 시작 위치 반환, 없으면 -1
#        return 1
#    else:
#        return 0
