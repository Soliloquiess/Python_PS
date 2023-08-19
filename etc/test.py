import random

def givehint(usernum_list, ground):  # 이전 예측과의 비교 및 가장 가까운 입력값 출력 함수
    global compnum
    global minnum
    if abs(compnum - usernum_list[-1]) <= minnum[-1]:  # 가장 가까운 입력값 출력
        minnum = [usernum_list[-1], abs(compnum - usernum_list[-1])]

    if ground > 3:
        if abs(compnum - usernum_list[-1]) > abs(compnum - usernum_list[-2]):  # 이전 예측과의 비교
            print("이전 예측보다 더 멀어졌습니다. 다시 생각해 보세요. ")
        elif abs(compnum - usernum_list[-1]) < abs(compnum - usernum_list[-2]):
            print("이전 예측보다 더 가까워졌습니다. 다시 생각해 보세요. ")
        else:
            print("다시 생각해 보세요. ")

        print("지금까지 가장 가까운 입력값: ", minnum[-2])

    else:
        print("다시 생각해 보세요. ")
    return None


def numcompare(usernum_list, ground):
    global compnum
    if compnum == usernum_list[-1]:
        print("정답!\n컴퓨터의 랜덤 숫자: ", compnum)
        return True
    elif compnum > usernum_list[-1]:
        print("Up!")
        givehint(usernum_list, ground)
        return False
    else:
        print('Down!')
        givehint(usernum_list, ground)
        return False


def samenuminput(usernum_list, num):
    if len(usernum_list) == 0:
        return False
    else:
        for i in range(len(usernum_list)):
            if num == usernum_list[i]:
                return True
            else:
                continue
        return False



def numgame(usernum_list, ground):
    while True:
        ground += 1
        print("\n", ground, "번째 시도")
        num = input("예상하는 숫자를 입력하세요 ")

        if not num.isdigit():
            print("숫자만 입력하세요 ")
            continue

        if not int(num) >= 0 and int(num) < 101:
            print("0~100 사이의 수만 입력하세요. ")
            continue

        if samenuminput(usernum_list, int(num)):  # 이전 입력값을 다시 입력한 경우
            print("이전에 입력했던 숫자입니다. 다시 입력하세요 ")
            continue

        usernum_list.append(int(num))
        print(usernum_list)
        result = numcompare(usernum_list, ground)
        if result:
            print("게임 종료!")
            break

global compnum
compnum = int(random.randint(0, 100))
global minnum
minnum = [101, 101]  # 임의 값 설정 minnum=[가장 가까운 입력값, 거리]
usernum_list = []
ground = 0
numgame(usernum_list, ground)