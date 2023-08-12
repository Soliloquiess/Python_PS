#1.
import re

def inputValueCheck(number):
    if not number:
        print("이름 혹은 점수를 입력해주세요.")
        return False

    if not re.match(r'^-?\d+$', number):
        print("숫자가 들어있지 않습니다. 다시 입력하세요")
        return False
    number = int(number)
    if(1 > number and number>50):
        print("1~50이하의 수만 입력해주세요")
        return False

    return True



def gugudan(number):
    try:
        if not inputValueCheck(number):
            return
        number = int(number)

        for i in range(1, 10):
            if i % 2 == 1:  # 홀수 번째만 출력
                result = number * i
                if result > 50:  # 50 이하인 것만 출력
                    # print(result)
                    print("해당 계산시 50을 넘어가고 있습니다. 50까지의 수까지만 계산됩니다.")
                    return
                print(f" {number} * {i} = {result}")

    except ValueError:
        print("잘못된 결과입니다.")
        return

number = input("숫자 입력하세요")
print(gugudan(number))


#2.

import random

def inputValueCheck(myPick):
    if not myPick:
        print("가위바위보에 해당하는 문자 또는 숫자를 입력해주세요.")
        return False

    rsp_pick = ["가위", "바위", "보"]
    num_to_rsp = {"0": "가위", "1": "바위", "2": "보"}

    if myPick not in rsp_pick and myPick not in num_to_rsp:
        print("잘못된 입력 요소입니다. 가위, 바위, 보, 0, 1, 2 중 하나만 선택하세요.")
        return False

    if myPick in num_to_rsp:
        myPick = num_to_rsp[myPick]

    return myPick


def rsp_game(games):
    try:
        if (games.isdigit() == False):
            print("숫자 잘못 입력하였습니다.")
            return
        rounds = int(games)
        if rounds <= 0:
            print("1 이상의 양수를 입력해주세요.")
            return
        winCount = 0
        loseCount = 0
        drawCount = 0


        for i, _ in enumerate(range(rounds), start=1):
            myPick = input("가위(0), 바위(1), 보(2) 중 하나를 선택하세요: ")
            myPick = inputValueCheck(myPick)
            while not myPick:
                myPick = input("다시 선택하세요: ")
                myPick = inputValueCheck(myPick)

            computerPick = random.choice(["가위", "바위", "보"])

            if myPick == computerPick:
                drawCount += 1
                print(f"{i} 번째 판 무승부, 당신이 {myPick}을 내어 {computerPick} 을 낸 컴퓨터를 상대로 비겼습니다.")
            elif (
                (myPick == "가위" and computerPick == "보")
                or (myPick == "바위" and computerPick == "가위")
                or (myPick == "보" and computerPick == "바위")
            ):
                winCount += 1
                print(f"{i} 번째 판 승리, 당신이 {myPick}을 내어 {computerPick} 을 낸 컴퓨터를 상대로 이겼습니다.")
            else:
                loseCount += 1
                print(f"{i} 번째 판 패배, 당신이 {myPick}을 내어 {computerPick} 을 낸 컴퓨터를 상대로 패배하였습니다.")

        print(f"\n총 전적: 이긴 횟수 - {winCount}, 진 횟수 - {loseCount}, 무승부 횟수 - {drawCount}")

    except ValueError:
        print("잘못된 결과입니다.")


while True :
    games = int(input('몇 판을 진행하시겠습니까? : '))
    if games >= 1 :
        break
    else :
        print('다시 입력해주세요')
        continue
games = str(games)
rsp_game(games)


#3.

def is_valid_input(n, m):
    if not n or not m:
        print("입력값이 없습니다. 입력해주세요.")
        return False

    if not n.isdigit() or not m.isdigit():
        print("숫자가 들어있지 않습니다. 다시 입력하세요.")
        return False

    return True

def find_even_numbers(n, m):
    try:
        if not is_valid_input(n, m):
            return

        n = int(n)
        m = int(m)

        if n > m:
            n, m = m, n

        numberList = [num for num in range(n, m + 1)]

        centerIndex = len(numberList) // 2

        if len(numberList) % 2 == 1:
            center_value = numberList[centerIndex]
        else:
            center_value = (numberList[centerIndex] + numberList[centerIndex - 1]) / 2

        print(f"center_value: {center_value}")

        for num in numberList:
            if num % 2 == 0:  # Check if the number is even
                print(num, "짝수")
                if num == center_value:
                    print(center_value, "중앙값")

    except ValueError:
        print("잘못된 결과입니다.")

n = input("첫 번째 수 입력: ")
m = input("두 번째 수 입력: ")
find_even_numbers(n, m)



# def is_valid_input(n, m):
#     if not n or not m:
#         print("입력값이 없습니다. 입력해주세요.")
#         return False
#
#     if not n.isdigit() or not m.isdigit():
#         print("숫자가 들어있지 않습니다. 다시 입력하세요")
#         return False
#
#     return True
#
# def find_even_numbers(n, m):
#     try:
#         if not is_valid_input(n, m):
#             return
#
#         n = int(n)
#         m = int(m)
#
#         even_numbers = [num for num in range(n, m + 1) if num % 2 == 0]
#
#         center_value = (float(n) + float(m)) / 2
#         if center_value % 2 == 0 :
#             center_value = int(center_value)
#         else:
#             center_value=None
#
#         print("짝수 리스트:", even_numbers)
#         if center_value is not None:
#             print("중앙값:", center_value)
#
#     except ValueError:
#         print("잘못된 결과입니다.")
#
# n, m = input("첫 번째 수 입력: "), input("두 번째 수 입력: ")
# find_even_numbers(n, m)


#4.

def is_valid_input(n, m):
    if not n or not m:
        print("입력값이 없습니다. 입력해주세요.")
        return False

    if not n.isdigit() or not m.isdigit():
        print("숫자가 들어있지 않습니다. 다시 입력하세요")
        return False

    return True

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def count_prime_number(n, m):
    try:
        if not is_valid_input(n, m):
            return

        n = int(n)
        m = int(m)

        prime_count = 0

        for num in range(n, m + 1):
            if is_prime(num):
                prime_count += 1
                print(f"{num}은 소수입니다.")

        print("소수개수:", prime_count)

    except ValueError:
        print("잘못된 결과입니다.")

n = input("첫 번째 수 입력: ")
m = input("두 번째 수 입력: ")
count_prime_number(n, m)
