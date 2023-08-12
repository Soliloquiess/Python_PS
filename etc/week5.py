import os
import random
import msvcrt


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_menu():
    clear_screen()
    print("┏━━━━━━━━━━━━┓")
    print("┃ 배스킨 라빈스 31 게임      ┃")
    print("┃                                       ┃")
    print("┃ 1.게임 시작 (초급)           ┃")
    print("┃ 2.게임 시작 (중급)           ┃")
    print("┃ 3.게임 전적                     ┃")
    print("┃ 0.종료                             ┃")
    print("┗━━━━━━━━━━━━┛")


def main():
    gCnt = 0
    winCnt = 0

    while True:
        clear_screen()
        print_menu()
        selMenu = int(input(" 선택 > "))

        if selMenu < 0 or selMenu > 3:
            continue

        if selMenu == 0:
            return

        if selMenu == 3:
            print("★ {}전 {}승 {}패 ★".format(gCnt, winCnt, gCnt - winCnt))
            input("Press Enter to continue...")
            continue

        gCnt += 1
        gameNum = 0

        while True:
            clear_screen()

            if selMenu == 1:
                print("\t [초급] 숫자 개수 (1~3) >", end=" ")
            elif selMenu == 2:
                print("\t [중급] 숫자 개수 (1~3) >", end=" ")

            player = int(input())
            if player < 1 or player > 3:
                continue

            for _ in range(player):
                gameNum += 1
                print("{:2d} Player".format(gameNum))
                if gameNum == 30:
                    print("\n ☆ 이겼습니다. 축하합니다. ☆")
                    winCnt += 1
                    break
                if gameNum >= 31:
                    print("\n ▽ 졌습니다. 다음 기회에... ▽")
                    break

            if gameNum == 29:
                com = 1
            elif gameNum == 28:
                com = 2
            elif gameNum == 27:
                com = 3
            else:
                com = random.randint(1, 3)

            for _ in range(com):
                gameNum += 1
                print("{:2d} Computer".format(gameNum))
                if gameNum == 30:
                    print("\n ▽ 컴퓨터가 이겼습니다. 다음 기회에... ▽")
                    break


if __name__ == "__main__":
    main()
