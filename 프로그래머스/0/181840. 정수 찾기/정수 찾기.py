def solution(num_list, n):
    if n in num_list:  # in 사용
        return 1
    else:
        return 0


#def solution(num_list, n):
#    for i in range(len(num_list)):
#        if num_list[i] == n:  # n과 일치하면
#            return 1          # 1 반환
#    return 0                  # 끝까지 없으면 0 반환
