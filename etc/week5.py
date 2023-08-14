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
