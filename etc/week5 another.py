
import random

randomNum = 56
mylist = []
count = 0
max = 100
min = 0
while True:
    count = count + 1
    userInput = int(input("숫자를 입력하세요:"))

    if userInput in mylist:
        print("이미 예측에 사용된 숫자입니다.")
        continue

    mylist.sort()
    print(mylist)
    if userInput > randomNum:
        print("Down!")
        if count > 1 and userInput > max:

            print("앞선 예측보다 큰 숫자입니다. \n현재 정답에 가까운 최댓값은", max, "입니다.")
            continue
        else:

            max = userInput

    elif userInput < randomNum:
        print("Up!")
        if count > 1 and userInput < min:

            print("앞선 예측보다 작은 숫자입니다. \n현재 정답에 가까운 최솟값은", min, "입니다.")
            continue
        else:

            min = userInput

    elif userInput == randomNum:
        break
    mylist.append(userInput)

print("정답입니다.", count, "차 시도에 성공하셨습니다. 게임을 종료합니다.")