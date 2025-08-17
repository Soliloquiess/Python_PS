def solution(date1, date2):
    return 1 if tuple(date1) < tuple(date2) else 0
#리스트 끼리는 비교 불가능, 그래서 튜플로 만들어서 비교


#def solution(date1, date2):
#    if date1[0] < date2[0]:   # 연도 비교
#        return 1
#    elif date1[0] > date2[0]:
#        return 0
#    else:  # 연도가 같으면
#        if date1[1] < date2[1]:  # 월 비교
#            return 1
#        elif date1[1] > date2[1]:
#            return 0
#        else:  # 월도 같으면
#            if date1[2] < date2[2]:  # 일 비교
#                return 1
#            else:
#                return 0