#5.1

import random


def is_valid_input(n):
    if not n:
        print("입력값이 없습니다. 입력해주세요.")
        return False

    if not n.isdigit():
        print("숫자가 들어있지 않습니다. 다시 입력하세요.")
        return False

    return True


def main():
    gameCnt = 0
    winCnt = 0

    while True:

        gameCnt += 1
        gameNum = 0
        numberList = []
        chkFlag = True;
        while True:
            playerInput = input("\t 숫자 입력 (공백으로 구분, 최대 3개) :: ")
            playerNumbers = playerInput.split()  # 공백으로 분리하여 리스트 생성
            lenPN = len(playerNumbers)
            playerNumbersList = []

            for num in playerInput.split():
                if not num.isdigit():
                    print("잘못된 입력입니다. 숫자를 입력하세요.")
                    chkFlag = False
                    break
                num = int(num)
                if num in numberList:
                    print("이미 입력한 숫자입니다. 다른 숫자를 입력하세요.")
                    chkFlag = False
                    break
                if num > (numberList[-1] + 3 if numberList else 3):
                    print("입력할 수 있는 범위를 초과하였습니다.")
                    chkFlag = False
                    break
                playerNumbersList.append(num)
            if(chkFlag == False):
                break;
            print(f"{len(playerNumbers)}");
            if len(playerNumbers) == 0:
                continue

            if lenPN > 3:
                print("3개 이상의 숫자를 입력하셨습니다. 최대 3개까지만 입력 가능합니다.")
                continue
            print(f"학생: {len(playerNumbersList)} ")
            numberList.extend(playerNumbersList)

            useNumber = playerNumbersList[0]
            if useNumber <= gameNum:
                print("현재 수 보다 큰 수를 입력해주세요")
                continue

            for i in playerNumbersList:
                gameNum += 1
                print("{:2d} Player".format(gameNum))
                if gameNum == 30:
                    print("\n ※ 플레이어 승리 ※")
                    winCnt += 1
                    break

            if gameNum == 29:
                com = 1
            elif gameNum == 28:
                com = 2
            elif gameNum == 27:
                com = 3
            else:
                com = random.randint(1, 3)

            for j in range(com):
                gameNum += 1
                numberList.append(gameNum)
                print("{:2d} Computer".format(gameNum))
                if gameNum == 30:
                    print("\n※  컴퓨터의 승리 ※ ")
                    break

            if gameNum >= 30:
                print("\n ※ 게임 끝 ※")
                break

            print("현재까지 입력된 숫자 리스트:", numberList)


if __name__ == "__main__":
    main()


#5.2


def grader(s, a):   #s= 학생 답. # a = 정답지 . 명시된 변수 조건 그지같네

    scores = []

    for student in s:
        name, answer = student.split(',')
        score = 0
        for i in range(len(answer)):
            if answer[i] == str(a[i]):
                score += 10
        scores.append((name, score))

    scores.sort(key=lambda x: x[1], reverse=True)

    for rank, (name, score) in enumerate(scores, start=1):
        print(f"학생: {name} 점수: {score}점 {rank}등")


with open('week5Input.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    s = [line.strip() for line in lines]

# 정답지
a = [3, 2, 4, 2, 5, 2, 4, 3, 1, 2]


if __name__ == "__main__":
    grader(s, a)




#5.3

import random

count = 0
randomNum = random.randint(1, 100)
checklist = []
uplist = []
downlist = []


def is_valid_input(n):
    if not n:
        print("입력값이 없습니다. 입력해주세요.")
        return False

    if not n.isdigit():
        print("숫자가 들어있지 않습니다. 다시 입력하세요.")
        return False

    number = int(n)
    if not 1 <= number <= 100:
        return False

    if number in checklist:
        print("이미 입력한 숫자입니다. 다시 입력하세요.")
        return False

    return True


def finding():
    global count, randomNum, checklist

    while True:
        userInput = input("숫자 입력: ")
        count += 1
        print(f"시도 횟수 : {count}회")

        if is_valid_input(userInput):
            userNum = int(userInput)

            checklist.append(userNum)
            checklist.sort()  # checklist를 정렬
            print(randomNum)
            if randomNum > userNum:
                print("UP!")
                uplist.append(userNum)
                uplist.sort()

                if userNum < uplist[-1]:
                    print(uplist[-1])
                    print(f"앞선 예측보다 작은 숫자입니다. 더 큰 수를 고민해보세요. 지금까지 가장 가까운 수는 {uplist[-1]} 입니다.")
                    continue

            elif randomNum < userNum:
                print("DOWN!")
                downlist.append(userNum)
                downlist.sort()

                if userNum > downlist[0]:
                    print(downlist[0])
                    print(f"앞선 예측보다 큰 숫자입니다. 더 작은 수를 고민해보세요. 지금까지 가장 가까운 수는 {downlist[0]} 입니다.")
                    continue
            else:
                print("정답!")
                print(f"총 시도 횟수 : {count + 1}회")
                break



        else:
            print("1 ~ 100 사이의 숫자를 입력해주세요.")


if __name__ == "__main__":
    finding()


#5.4




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

    if day < 1 or day > monthDay[month]:
        print("유효하지 않은 일자입니다. 해당 월의 유효한 범위 내에서 입력하세요.")
        return False

    if date not in dates:
        print("유효하지 않은 요일입니다. '월요일'부터 '일요일'까지의 값을 입력하세요.")
        return False

    return True


def calculate(year, month, day, date, monthDay, dates): #🤔변수명 뭐하지
    currentYear  = int(year)
    currentMonth  = int(month)
    currentDay  = int(day)
    currentDate  = dates.index(date)

    for i in range(100):
        daysOfmonth  = monthDay[currentMonth]

        if currentDay + 1 > daysOfmonth :
            currentMonth += 1
            if currentMonth > 12:
                currentYear += 1
                currentMonth = 1
            currentDay = 1
        else:
            currentDay += 1

        currentDate = (currentDate + 1) % 7
    currentDate = dates[currentDate]
    return currentYear, currentMonth, currentDay, currentDate


def main():
    monthDay  = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    dates = ["월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일"]
    while True:
        year, month, day, date = input("연도 월 일 요일을 입력하세요 (예: 2023 08 13 수요일): ").split()

        if is_valid_input(year, month, day, date, monthDay, dates):

            resultYear, resultMonth, resultDay, resultDate = calculate(year, month, day, date, monthDay, dates)

            print(f"100일 뒤의 날짜는 {resultYear}년 {resultMonth}월 {resultDay}일 {resultDate}입니다.")
            break


if __name__ == "__main__":
    main()
