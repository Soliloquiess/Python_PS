
def is_valid_input(year, month, day, date, monthDay, dates):
    if not year.isdigit():
        print("년은 숫자로 입력되어야 합니다.")
        return False

    if not month.isdigit():
        print("월은 숫자로 입력되어야 합니다.")
        return False

    if not day.isdigit():
        print("일은 숫자로 입력되어야 합니다.")
        return False

    year = int(year)
    month = int(month)
    day = int(day)

    if year < 1970:
        print("유효하지 않은 년입니다. 1970년 이후로 입력하세요.")
        return False

    if month < 1 or month > 12:
        print("유효하지 않은 월입니다. 1부터 12 사이의 값을 입력하세요.")
        return False

    if day < 1 or day > monthDay[month - 1]:
        print("유효하지 않은 일자입니다. 해당 월의 유효한 범위 내에서 입력하세요.")
        return False

    if date not in dates:
        print("유효하지 않은 요일입니다. '월요일'부터 '일요일'까지의 값을 입력하세요.")
        return False

    return True


def calculate(year, month, day, date, monthDay, dates): #변수명 뭐하지
    resultYear  = int(year)
    resultMonth  = int(month)
    resultDay  = int(day)
    resultDate  = dates.index(date)

    for i in range(100):
        daysOfmonth  = monthDay[resultMonth - 1]

        if resultDay + 1 > daysOfmonth :
            resultMonth += 1
            resultDay = 1
            if resultMonth > 12:
                resultYear += 1
                resultMonth = 1
        else:
            resultDay += 1

        resultDate = (resultDate + 1) % 7
    resultDate = dates[resultDate]
    return resultYear, resultMonth, resultDay, resultDate


def main():
    monthDay  = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    dates = ["월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일"]
    while True:
        year, month, day, date = input("연도 월 일 요일을 입력하세요 (예: 2023 08 14 월요일): ").split()

        if is_valid_input(year, month, day, date, monthDay, dates):

            resultYear, resultMonth, resultDay, resultDate = calculate(year, month, day, date, monthDay, dates)

            print(f"100일 뒤의 날짜는 {resultYear}년 {resultMonth}월 {resultDay}일 {resultDate}입니다.")
            break


if __name__ == "__main__":
    main()
