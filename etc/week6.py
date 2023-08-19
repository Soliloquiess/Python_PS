num = []

def number():
    my = input("My turn-숫자를 입력하세요(최대 3개까지, 스페이스바로 구분):")
    my2 = my.split()

    for i in range(0, len(my2)):
        num.append(my2[i])
        if "10" in num:
            return "컴"

    import random
    computer_turn_num = random.randint(1, 3)

    for i in range(computer_turn_num):
        n = str(int(num[-1]) + 1)
        print(n)
        num.append(n)

        if "10" in num:
            return "플"

    print("현재 숫자:", num[-1])


while True:
    if "10" in num:
        break

    value = number()

    if value == "컴":
        print("컴퓨터 승리!")
    elif value == "플":
        print("플레이어 승리!")
