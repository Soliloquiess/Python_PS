import os
import random
import msvcrt

def is_valid_input(n):
    if not n or not m:
        print("입력값이 없습니다. 입력해주세요.")
        return False

    if not n.isdigit() :
        print("숫자가 들어있지 않습니다. 다시 입력하세요.")
        return False

    return True

# def clear_screen():
#     os.system('cls' if os.name == 'nt' else 'clear')

def print_menu():
    # clear_screen()
    print("======================")
    print(" 1.게임 시작 ")
    print(" 2.게임 전적 ")
    print(" 0.종료     ")
    print("======================")

def main():
    gameCnt = 0
    winCnt = 0

    while True:
        # clear_screen()
        print_menu()
        selMenu = int(input(" 선택 > "))
        is_valid_input(selMenu)
        if selMenu < 0 or selMenu > 3:
            continue

        if selMenu == 0:
            return

        if selMenu == 2:
            print(" {}전 {}승 {}패 ".format(gameCnt, winCnt, gameCnt - winCnt))
            input("Press Enter to continue...")
            continue

        gameCnt += 1
        gameNum = 0

        while True:
            if selMenu == 1:
                player_input = input("\t 숫자 입력 (공백으로 구분) :: ")
                player_numbers = [int(num) for num in player_input.split()]

                # extracted_number1 = int(player_input[0])
                # extracted_number2 = int(player_input[-1])
                extracted_number1 = int(player_input.split()[0])
                print("gameNUM",gameNum);
                print("extracted_number1",extracted_number1);
                if(extracted_number1 <= gameNum):
                    print("현재 수 보다 큰 수 입력해주세요")
                    continue

                # if any(num < 1 or num > 3 for num in player_numbers):
                #     print("잘못된 입력입니다. 숫자는 1에서 3 사이어야 합니다.")
                #     continue

                for player in player_numbers:
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

                for i in range(com):
                    gameNum += 1
                    print("{:2d} Computer".format(gameNum))
                    if gameNum == 30:
                        print("\n ▽ 컴퓨터가 이겼습니다. 다음 기회에... ▽")
                        break

                if gameNum >= 30:
                    print("\n ※ 게임 끝 ※")
                    break

if __name__ == "__main__":
    main()
