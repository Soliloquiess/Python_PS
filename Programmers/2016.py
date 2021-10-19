def solution(a, b):
    week = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    month_sum = []
    for idx, value in enumerate(month):
        if idx == 0:
            month_sum.append(month[0])
        else:
            month_sum.append(month_sum[idx - 1] + month[idx])


    if a-1==0:
        answer = week[(0 + b - 1) % 7]
    else:
        answer = week[(month_sum[a - 2] + b - 1) % 7]
    return answer

print(solution(5,24))
# https://yaneodoo2.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-level-1-2016%EB%85%84

# # 문제가 개편되었습니다. 이로 인해 함수 구성이나 테스트케이스가 변경되어, 과거의 코드는 동작하지 않을 수 있습니다.
# # 새로운 함수 구성을 적용하려면 [코드 초기화] 버튼을 누르세요. 단, [코드 초기화] 버튼을 누르면 작성 중인 코드는 사라집니다.
# def getDayName(a,b):
#     months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     days = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
#     return days[(sum(months[:a-1])+b-1)%7]
#
# #아래 코드는 테스트를 위한 출력 코드입니다.
# print(getDayName(5,24))



# 문제가 개편되었습니다. 이로 인해 함수 구성이나 테스트케이스가 변경되어, 과거의 코드는 동작하지 않을 수 있습니다.
# 새로운 함수 구성을 적용하려면 [코드 초기화] 버튼을 누르세요. 단, [코드 초기화] 버튼을 누르면 작성 중인 코드는 사라집니다.
def getDayName(a,b):
    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    return days[(sum(months[:a-1])+b-1)%7]

#아래 코드는 테스트를 위한 출력 코드입니다.
print(getDayName(5,24))
