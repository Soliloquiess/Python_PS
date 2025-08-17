def solution(a, b):
    if a % 2 == 1 and b % 2 == 1:  # 두 수 모두 홀수
        return a**2 + b**2
    elif a % 2 == 1 or b % 2 == 1:  # 한 수만 홀수
        return 2 * (a + b)
    else:  # 둘 다 홀수가 아님
        return abs(a - b)


#def solution(a, b):
    # 두 수가 홀수인지 확인
#    a_odd = a % 2 == 1
#    b_odd = b % 2 == 1

#    if a_odd and b_odd:  # 두 수 모두 홀수
#        score = a * a + b * b
#    elif a_odd or b_odd:  # 한 수만 홀수
#        score = 2 * (a + b)
#    else:  # 둘 다 홀수가 아님
#        score = a - b
#       if score < 0:     # 절댓값 계산
#            score = -score
#    return score
