import random

def inputValueCheck(myPick):
    if not myPick:
        print("나이 혹은 결제수단을 입력해주세요.")
        return False

    if (myPick.isalpha() == False):
        print("입력한 요소 중 문자만 들어있지 않습니다. 다시 입력하세요")
        return False

    if myPick not in ["가위", "바위", "보"]: #if not (myPick == "가위" or myPick == "바위" or myPick == "보"):
        print("잘못된 입력 요소입니다. 가위 바위 보 중 하나만 내세요")
        return False;
    return True


def rsp(myPick):
    try:
        if not inputValueCheck(myPick):
            return
        result = {}
        rspPick = ["가위", "바위", "보"]
        computerPick = random.choice(rspPick)

        if ((myPick == "가위" and computerPick == "보") or (myPick == "바위" and computerPick == "가위") or (myPick == "보" and computerPick == "바위")):
            print(f"당신이 {myPick}을 내어 {computerPick} 을 낸 컴퓨터를 상대로 이겼습니다.")

        elif ((myPick == "가위" and computerPick == "바위") or (myPick == "바위" and computerPick == "보") or (myPick == "보" and computerPick == "가위")):
            print(f"당신이 {myPick}을 내어 {computerPick} 을 낸 컴퓨터를 상대로 패배하였습니다.")
        else:
            print(f"당신이 {myPick}을 내어 {computerPick} 을 낸 컴퓨터를 상대로 무승부입니다.")

    except ValueError:
        print("잘못된 결과입니다. FFFF")
        return


myPick = input("가위바위보 시작. 입력하세요: ")
print(rsp(myPick))