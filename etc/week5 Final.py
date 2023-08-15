
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
                chkFlag = True;
                continue;
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

                print(f"Player 낸 숫자 : {gameNum}")
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
                print(f"computer 낸 숫자 : {gameNum}")
                if gameNum == 30:
                    print("\n※  컴퓨터의 승리 ※ ")
                    break

            if gameNum >= 30:
                print("\n ※ 게임 끝 ※")
                break

            print("현재까지 입력된 숫자 리스트:", numberList)


if __name__ == "__main__":
    main()



# import random
#
#
# def is_valid_input(n):
#     if not n:
#         print("입력값이 없습니다. 입력해주세요.")
#         return False
#
#     if not n.isdigit():
#         print("숫자가 들어있지 않습니다. 다시 입력하세요.")
#         return False
#
#     return True
#
#
# def Menu():
#     print(" 1.게임 시작 ")
#     print(" 2.게임 전적 ")
#     print(" 0.종료     ")
#
#
# def main():
#     gameCnt = 0
#     winCnt = 0
#
#     while True:
#         Menu()
#         selMenu = input(" 선택 > ")
#         if not is_valid_input(selMenu) or selMenu < '0' or selMenu > '2':
#             print("잘못 입력했습니다. 재입력 하세요")
#             continue
#
#         if selMenu == '0':
#             return
#
#         if selMenu == '2':
#             print(" {}전 {}승 {}패 ".format(gameCnt, winCnt, gameCnt - winCnt))
#             continue
#
#         gameCnt += 1
#         gameNum = 0
#         numberList = []
#
#         while True:
#             if selMenu == '1':
#                 playerInput = input("\t 숫자 입력 (공백으로 구분, 최대 3개) :: ")
#                 playerNumbers = []
#                 for num in playerInput.split():
#                     if not num.isdigit():
#                         print("잘못된 입력입니다. 숫자를 입력하세요.")
#                         break
#                     num = int(num)
#                     if num in numberList:
#                         print("이미 입력한 숫자입니다. 다른 숫자를 입력하세요.")
#                         break
#                     if num > (numberList[-1] + 3 if numberList else 3):
#                         print("입력할 수 있는 범위를 초과하였습니다.")
#                         break
#                     playerNumbers.append(num)
#
#                 if len(playerNumbers) == 0:
#                     continue
#
#                 if len(playerNumbers) > 3:
#                     print("3개 이상의 숫자를 입력하셨습니다. 최대 3개까지만 입력 가능합니다.")
#                     continue
#
#                 numberList.extend(playerNumbers)
#
#                 useNumber = playerNumbers[0]
#                 if useNumber <= gameNum:
#                     print("현재 수 보다 큰 수를 입력해주세요")
#                     continue
#
#                 for i in playerNumbers:
#                     gameNum += 1
#                     print("{:2d} Player".format(gameNum))
#                     if gameNum == 30:
#                         print("\n ※ 플레이어 승리 ※")
#                         winCnt += 1
#                         break
#
#                 if gameNum == 29:
#                     com = 1
#                 elif gameNum == 28:
#                     com = 2
#                 elif gameNum == 27:
#                     com = 3
#                 else:
#                     com = random.randint(1, 3)
#
#                 for j in range(com):
#                     gameNum += 1
#                     numberList.append(gameNum)
#                     print("{:2d} Computer".format(gameNum))
#                     if gameNum == 30:
#                         print("\n※  컴퓨터의 승리 ※ ")
#                         break
#
#                 if gameNum >= 30:
#                     print("\n ※ 게임 끝 ※")
#                     break
#
#             print("현재까지 입력된 숫자 리스트:", numberList)
#
#         print("플레이어와 컴퓨터의 입력 숫자:", numberList)
#
#
# if __name__ == "__main__":
#     main()




#
# import random
#
#
# def is_valid_input(n):
#     if not n:
#         print("입력값이 없습니다. 입력해주세요.")
#         return False
#
#     if not n.isdigit():
#         print("숫자가 들어있지 않습니다. 다시 입력하세요.")
#         return False
#
#     return True
#
#
# def Menu():
#     print(" 1.게임 시작 ")
#     print(" 2.게임 전적 ")
#     print(" 0.종료     ")
#
#
# def main():
#     gameCnt = 0
#     winCnt = 0
#
#     while True:
#         Menu()
#         selMenu = input(" 선택 > ")
#         if not is_valid_input(selMenu) or selMenu < '0' or selMenu > '2':
#             print("잘못 입력했습니다. 재입력 하세요")
#             continue
#
#         if selMenu == '0':
#             return
#
#         if selMenu == '2':
#             print(" {}전 {}승 {}패 ".format(gameCnt, winCnt, gameCnt - winCnt))
#             continue
#
#         gameCnt += 1
#         gameNum = 0
#
#         while True:
#             if selMenu == '1':
#                 playerInput = input("\t 숫자 입력 (공백으로 구분, 최대 3개) :: ")
#                 playerNumbers = []
#                 for num in playerInput.split():
#                     if not num.isdigit():
#                         print("잘못된 입력입니다. 숫자를 입력하세요.")
#                         break
#                     playerNumbers.append(int(num))
#
#                 if len(playerNumbers) == 0:
#                     continue
#
#                 if len(playerNumbers) > 3:
#                     print("3개 이상의 숫자를 입력하셨습니다. 최대 3개까지만 입력 가능합니다.")
#                     continue
#
#                 if len(set(playerNumbers)) != len(playerNumbers):
#                     print("중복된 숫자가 있습니다. 중복되지 않은 숫자를 입력하세요.")
#                     continue
#
#                 useNumber = playerNumbers[0]
#                 print("gameNUM", gameNum)
#                 print("useNumber", useNumber)
#                 if useNumber <= gameNum:
#                     print("현재 수 보다 큰 수 입력해주세요")
#                     continue
#
#                 for i in playerNumbers:
#                     gameNum += 1
#                     print("{:2d} Player".format(gameNum))
#                     if gameNum == 30:
#                         print("\n ※ 플레이어 승리 ※")
#                         winCnt += 1
#                         break
#
#                 if gameNum == 29:
#                     com = 1
#                 elif gameNum == 28:
#                     com = 2
#                 elif gameNum == 27:
#                     com = 3
#                 else:
#                     com = random.randint(1, 3)
#
#                 for j in range(com):
#                     gameNum += 1
#                     print("{:2d} Computer".format(gameNum))
#                     if gameNum == 30:
#                         print("\n※  컴퓨터의 승리 ※ ")
#                         break
#
#                 if gameNum >= 30:
#                     print("\n ※ 게임 끝 ※")
#                     break
#
#
# if __name__ == "__main__":
#     main()


# import os
# import random
# import msvcrt
#
# def is_valid_input(n):
#     if not n:
#         print("입력값이 없습니다. 입력해주세요.")
#         return False
#
#     if not n.isdigit() :
#         print("숫자가 들어있지 않습니다. 다시 입력하세요.")
#         return False
#
#     return True
#
# def print_menu():
#     print(" 1.게임 시작 ")
#     print(" 2.게임 전적 ")
#     print(" 0.종료     ")
#
# def main():
#     gameCnt = 0
#     winCnt = 0
#
#     while True:
#         print_menu()
#         selMenu = input(" 선택 > ")
#         is_valid_input(selMenu)
#         if selMenu < '0' or selMenu > '2':
#             print("잘못 입력했습니다. 재입력 하세요")
#             continue
#
#         if selMenu == '0':
#             return
#
#         if selMenu == '2':
#             print(" {}전 {}승 {}패 ".format(gameCnt, winCnt, gameCnt - winCnt))
#
#             continue
#
#         gameCnt += 1
#         gameNum = 0
#
#         while True:
#             if selMenu == '1':
#                 player_input = input("\t 숫자 입력 (공백으로 구분) :: ")
#                 player_numbers = [int(num) for num in player_input.split()]
#
#                 extracted_number1 = int(player_input.split()[0])
#                 print("gameNUM",gameNum);
#                 print("extracted_number1",extracted_number1);
#                 if(extracted_number1 <= gameNum):
#                     print("현재 수 보다 큰 수 입력해주세요")
#                     continue
#
#                 for i in player_numbers:
#                     gameNum += 1
#                     print("{:2d} Player".format(gameNum))
#                     if gameNum == 30:
#                         print("\n ※ 플레이어 승리 ※")
#                         winCnt += 1
#                         break
#
#
#                 if gameNum == 29:
#                     com = 1
#                 elif gameNum == 28:
#                     com = 2
#                 elif gameNum == 27:
#                     com = 3
#                 else:
#                     com = random.randint(1, 3)
#
#                 for j in range(com):
#                     gameNum += 1
#                     print("{:2d} Computer".format(gameNum))
#                     if gameNum == 30:
#                         print("\n ▽ 컴퓨터가 이겼습니다. 다음 기회에... ▽")
#                         break
#
#                 if gameNum >= 30:
#                     print("\n ※ 게임 끝 ※")
#                     break
#
# if __name__ == "__main__":
#     main()

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


# def grader(s, a):   #s= 학생 답. # a = 정답지 . 명시된 변수 조건 그지같네
#     def calculate_score(student_answer):
#         score = 0
#         for i in range(len(student_answer)):
#             if student_answer[i] == str(a[i]):
#                 score += 10
#         return score
#
#     scores = []
#
#     for student in s:
#         name, answer = student.split(',')
#         # score = calculate_score(answer)
#         score = 0
#         for i in range(len(student_answer)):
#             if student_answer[i] == str(a[i]):
#                 score += 10
#         return score
#         scores.append((name, score))
#
#     scores.sort(key=lambda x: x[1], reverse=True)
#
#     for rank, (name, score) in enumerate(scores, start=1):
#         print(f"학생: {name} 점수: {score}점 {rank}등")
#
#
# with open('week5_input.txt', 'r', encoding='utf-8') as file:
#     lines = file.readlines()
#     s = [line.strip() for line in lines]
#
# # 정답지
# a = [3, 2, 4, 2, 5, 2, 4, 3, 1, 2]
#
# # 채점 및 결과 출력
# grader(s, a)



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



# import random
#
# randomNum = random.randint(1, 100)
# mylist = []
# count = 0
# max = 100
# min = 0
# while True:
#     count = count + 1
#     userInput = int(input("숫자를 입력하세요:"))
#
#     if userInput in mylist:
#         print("이미 예측에 사용된 숫자입니다.")
#         continue
#
#     mylist.sort()
#     print(mylist)
#     if userInput > randomNum:
#         print("Down!")
#         if count > 1 and userInput > max:
#
#             print("앞선 예측보다 큰 숫자입니다. \n현재 정답에 가까운 최댓값은", max, "입니다.")
#             continue
#         else:
#
#             max = userInput
#
#     elif userInput < randomNum:
#         print("Up!")
#         if count > 1 and userInput < min:
#
#             print("앞선 예측보다 작은 숫자입니다. \n현재 정답에 가까운 최솟값은", min, "입니다.")
#             continue
#         else:
#
#             min = userInput
#
#     elif userInput == randomNum:
#         break
#     mylist.append(userInput)
#
# print("정답입니다.", count, "차 시도에 성공하셨습니다. 게임을 종료합니다.")


#
# import random
#
# count = 0
# randomNum = random.randint(1, 100)
#
# def is_valid_input(n):
#     if not n:
#         print("입력값이 없습니다. 입력해주세요.")
#         return False
#
#     if not n.isdigit():
#         print("숫자가 들어있지 않습니다. 다시 입력하세요.")
#         return False
#
#     number = int(n)
#     if not 1 <= number <= 100:
#         return False
#     return True
#
# def finding():
#     global count, randomNum
#
#     while True:
#         userInput = input("숫자 입력: ")
#
#         if is_valid_input(userInput):
#             userNum = int(userInput)
#
#             if randomNum > userNum:
#                 print("UP!")
#             elif randomNum < userNum:
#                 print("DOWN!")
#             else:
#                 print("정답!")
#                 print(f"총 시도 횟수 : {count + 1}회")
#                 break
#             count += 1
#             print(f"시도 횟수 : {count}회")
#         else:
#             print("1 ~ 100 사이의 숫자를 입력해주세요.")
#
# if __name__ == "__main__":
#     finding()



# import random
#
# count = 0
# randomNum = random.randint(1, 100)
#
# def is_valid_input(n):
#     if not n:
#         print("입력값이 없습니다. 입력해주세요.")
#         return False
#
#     if not n.isdigit():
#         print("숫자가 들어있지 않습니다. 다시 입력하세요.")
#         return False
#     return True
#
# def finding():
#     global count, randomNum
#
#     while True:
#         userInput = input("숫자 입력: ")
#
#         if is_valid_input(userInput):
#             userNum = int(userInput)
#
#             if 1 <= userNum <= 100:
#                 if randomNum > userNum:
#                     print("UP!")
#                 elif randomNum < userNum:
#                     print("DOWN!")
#                 else:
#                     print("정답!")
#                     print(f"총 시도 횟수 : {count + 1}회")
#                     break
#                 count += 1
#                 print(f"시도 횟수 : {count}회")
#             else:
#                 print("1 ~ 100 사이의 숫자를 입력해주세요.")
#
# if __name__ == "__main__":
#     finding()
#
#


# import random
#
# counter = 0
# randomNumber = random.randint(1, 100)
#
# def finding():
#     global counter, randomNumber
#
#     userNumber = int(input("숫자를 예측해보세요: "))
#
#     if 1 <= userNumber <= 100:
#         if randomNumber > userNumber:
#             print("UP!")
#         elif randomNumber < userNumber:
#             print("DOWN!")
#         else:
#             print("\033[94m정답!\033[0m")  # 파란색으로 텍스트 출력
#         counter += 1
#         print(f"시도 횟수 : {counter}회")
#     else:
#         print("1 ~ 100 사이의 숫자를 입력해주세요.")
#
# def main():
#     while True:
#         finding()
#
# if __name__ == "__main__":
#     main()





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

    if day < 1 or day > monthDay[month - 1]:
        print("유효하지 않은 일자입니다. 해당 월의 유효한 범위 내에서 입력하세요.")
        return False

    if date not in dates:
        print("유효하지 않은 요일입니다. '월요일'부터 '일요일'까지의 값을 입력하세요.")
        return False

    return True


def calculate(year, month, day, date, monthDay, dates): #🤔변수명 뭐하지
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


#
# def is_valid_input(year, month, day, date, monthDay, dates):
#     if not year.isdigit():
#         print("년은 숫자로 입력되어야 합니다.")
#         return False
#
#     if not month.isdigit():
#         print("월은 숫자로 입력되어야 합니다.")
#         return False
#
#     if not day.isdigit():
#         print("일은 숫자로 입력되어야 합니다.")
#         return False
#
#     year = int(year)
#     month = int(month)
#     day = int(day)
#
#     if year < 1970:
#         print("유효하지 않은 년입니다. 1970년 이후로 입력하세요.")
#         return False
#
#     if month < 1 or month > 12:
#         print("유효하지 않은 월입니다. 1부터 12 사이의 값을 입력하세요.")
#         return False
#
#     if day < 1 or day > monthDay[month]:
#         print("유효하지 않은 일자입니다. 해당 월의 유효한 범위 내에서 입력하세요.")
#         return False
#
#     if date not in dates:
#         print("유효하지 않은 요일입니다. '월요일'부터 '일요일'까지의 값을 입력하세요.")
#         return False
#
#     return True
#
#
# def calculate(year, month, day, date, monthDay, dates): #🤔변수명 뭐하지
#     currentYear  = int(year)
#     currentMonth  = int(month)
#     currentDay  = int(day)
#     currentDate  = dates.index(date)
#
#     for i in range(100):
#         daysOfmonth  = monthDay[currentMonth]
#
#         if currentDay + 1 > daysOfmonth :
#             currentMonth += 1
#             if currentMonth > 12:
#                 currentYear += 1
#                 currentMonth = 1
#             currentDay = 1
#         else:
#             currentDay += 1
#
#         currentDate = (currentDate + 1) % 7
#     currentDate = dates[currentDate]
#     return currentYear, currentMonth, currentDay, currentDate
#
#
# def main():
#     monthDay  = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     dates = ["월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일"]
#     while True:
#         year, month, day, date = input("연도 월 일 요일을 입력하세요 (예: 2023 08 13 수요일): ").split()
#
#         if is_valid_input(year, month, day, date, monthDay, dates):
#
#             resultYear, resultMonth, resultDay, resultDate = calculate(year, month, day, date, monthDay, dates)
#
#             print(f"100일 뒤의 날짜는 {resultYear}년 {resultMonth}월 {resultDay}일 {resultDate}입니다.")
#             break
#
#
# if __name__ == "__main__":
#     main()

# def is_valid_input(n):
#     if not n:
#         print("입력값이 없습니다. 입력해주세요.")
#         return False
#
#     if not n.isdigit() :
#         print("숫자가 들어있지 않습니다. 다시 입력하세요.")
#         return False
#
#     return True
#
#
# def calculate(year, month, day, date):
#     monthDay = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     dates = ["월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일"]
#     currentYear = year
#     currentMonth = month
#     currentDay = day
#     currentDate = dates.index(date)
#     for i in range(100):
#         daysOfmonth = monthDay[currentMonth]
#
#         if currentDay + 1 > daysOfmonth:
#             currentMonth += 1
#             if currentMonth > 12:
#                 currentYear += 1
#                 currentMonth = 1
#             currentDay = 1
#         else:
#             currentDay += 1
#
#         currentDate = (currentDate + 1) % 7
#     currentDate = dates[currentDate]
#     return currentYear, currentMonth, currentDay, currentDate
#
#
# def main():
#     year, month, day, date = input("연도 월 일 요일을 입력하세요 (예: 2023 08 13 수요일): ").split()
#     year = int(year)
#     month = int(month)
#     day = int(day)
#
#     resultYear, resultMonth, resultDay, resultDate = calculate(year, month, day, date)
#
#     print(f"100일 뒤의 날짜는 {resultYear}년 {resultMonth}월 {resultDay}일 {resultDate}입니다.")
#
#
# if __name__ == "__main__":
#     main()



#
# def calculate_100th_day(year, month, day, date):
#     monthDay = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     dates = ["월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일"]
#     currentYear = year
#     currentMonth = month
#     currentDay = day
#     currentDate = dates.index(date)
#     for i in range(100):
#         daysOfmonth = monthDay[currentMonth]
#
#         if currentDay + 1 > daysOfmonth:
#             currentMonth += 1
#             if currentMonth > 12:
#                 currentYear += 1
#                 currentMonth = 1
#             currentDay = 1
#         else:
#             currentDay += 1
#
#         currentDate = (currentDate + 1) % 7
#     currentDate = dates[currentDate]
#     return currentYear, currentMonth, currentDay, currentDate
#
#
# def main():
#     year, month, day, date = input("연도 월 일 요일을 입력하세요 (예: 2023 08 13 수요일): ").split()
#     year = int(year)
#     month = int(month)
#     day = int(day)
#
#     resultYear, resultMonth, resultDay, resultDate = calculate_100th_day(year, month, day, date)
#
#     print(f"100일 뒤의 날짜는 {resultYear}년 {resultMonth}월 {resultDay}일 {resultDate}입니다.")
#
#
# if __name__ == "__main__":
#     main()
#
#
# #####
#
# from datetime import datetime, timedelta
#
# def get_date_from_user():
#     year = int(input("연도를 입력하세요: "))
#     month = int(input("월을 입력하세요: "))
#     day = int(input("일을 입력하세요: "))
#     return datetime(year, month, day)
#
# # 오늘 날짜 정보를 가져옵니다.
# now = datetime.now()
#
# # 사용자로부터 처음 만난 날의 날짜를 입력받습니다.
# first_day = get_date_from_user()
#
# # 오늘 날짜와 처음 만난 날 사이의 차이를 계산합니다.
# passed_time = now - first_day
# passed_day = passed_time.days
#
# print(f"{passed_day}일")
#
# def calc_date(days):
#     # 처음 만난 날에 일 수를 더합니다.
#     future = first_day + timedelta(days=days)
#
#     # 연도, 월, 일을 가져옵니다.
#     year = future.year
#     month = future.month
#     date = future.day
#
#     print(f"{year}년 {month}월 {date}일")
#
# # 여러 기념일을 계산하여 표시합니다.
# calc_date(100)
# calc_date(200)
# calc_date(365)
# calc_date(500)
#
#
#
