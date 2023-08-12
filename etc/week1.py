import sys
import datetime as dt


def get_integer_input(value):
    while True:
        try:
            value = int(input(value))
            return value
        except ValueError:
            print("잘못된 입력입니다. 숫자를 입력해주세요.")


def solution():
    year = dt.datetime.now()
    yearYY = year.year

    while True:
        birth = get_integer_input("몇년생인지 입력해주세요: ")
        birthChk = get_integer_input("생일이 지났습니까? 맞으면 0 아니면 -1: ")

        if birth < 1900 or birth > yearYY:
            print("잘못된 입력입니다. 출생 연도는 1900부터 현재 연도까지 입력해주세요.")
        elif birthChk not in (0, -1):
            print("잘못된 입력입니다. 생일 체크는 0이나 -1을 입력해주세요.")
        else:
            break

    if birthChk == 0:
        yearYY = yearYY - birth
    else:
        yearYY = yearYY - birth - 1

    return yearYY


print(solution())

# import sys
# import datetime as dt
#
# def solution():
#     year = dt.datetime.now()  # 현재 날짜 가져오는 내장 date함수
#     yearYY = year.year  # 현재 날짜 중 년도만 가져옴 YYYYMMDD HH:MM:SS 형식
#     while True:
#         try:
#             birth = int(input("몇년생인지 입력해주세요: "))
#             birthChk = int(input("생일이 지났습니까? 맞으면 0 아니면 -1: "))
#
#             if ((birth < 1900) or (birth > yearYY)):
#                 print("잘못된 입력입니다. 연도는 1900부터 현재년도 사이를 입력해주세요.")
#                 return
#             elif (birthChk != 0) and (birthChk != -1):
#                 print("잘못된 입력입니다. 생일 구분은 0 또는 -1만 입력해주세요")
#                 return
#             else:
#                 break;
#         except ValueError:
#             print("잘못된 입력입니다. 숫자를 입력해주세요.")
#             return;
#
#     if birthChk == 0:
#         yearYY = yearYY - birth
#     else:
#         yearYY = yearYY - birth - 1
#     return yearYY  # 나이로 리턴
#
# print(solution())
