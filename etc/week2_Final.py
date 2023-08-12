# Mission2

#1. 학점 계산기

def inputValueCheck(name, score):
    if not name or not score:
        print("이름 혹은 점수를 입력해주세요.")
        return False

    if (name.isalpha() == False):
        print("이름에 문자만 들어있지 않습니다. 다시 입력하세요")
        return False

    if (score.isdigit() == False):
        print("성적에 숫자만 들어있지 않습니다. 다시 입력하세요")
        return False
    score = int(score)
    if(score < 0 or score>100):
        print("잘못된 점수입니다.")
        return False;

    return True;


def grader(name, score):
    try:
        if not inputValueCheck(name, score):
            return
        score = int(score);
        result = {};

        gradeList = {
            (95, 100): 'A+',
            (90, 94): 'A',
            (85, 89): 'B+',
            (80, 84): 'B',
            (75, 79): 'C',
            (70, 74): 'C+',
            (65, 69): 'D+',
            (60, 64): 'D',
            (0,59) : '60점 미만'
        }


        for (low, high), grade in gradeList.items():
            if low <= score <= high:
                result = {
                    '이름': name,
                    '점수':score,
                    '학점': grade
                }

                print(f"학생이름: {name}")
                print(f"점수: {score}") #print("점수: " + str(score));
                print(f"학점: {grade}")


                return result

    except ValueError:
        print("잘못된 결과입니다. FFFF")
        return;

name, score = input("이름, 점수 입력하세요").split()
print(grader(name, score));

#2.

def inputValueCheck(money):
    if not money:
        print("월급을 입력해주세요.")
        return False

    if not money.isdigit():
        print("월급에는 숫자만 들어있어야 합니다. 다시 입력하세요")
        return False
    return True

def calculate_tax(salary):
    # 세율을 구간별로 저장
    rates = {
        1200 * 10 ** 4: 0.06,
        4600 * 10 ** 4: 0.15,
        8800 * 10 ** 4: 0.24,
        15000 * 10 ** 4: 0.35,
        30000 * 10 ** 4: 0.38,
        50000 * 10 ** 4: 0.40,
    }
    # 기본 세율은 0.42로 설정
    default_tax_rate = 0.42

    # 세율 구하기
    tax_rate = default_tax_rate
    for ratesSalary, rate in rates.items():
        if salary <= ratesSalary:
            tax_rate = rate
            break

    return tax_rate

def yearly_payment(money):
    try:
        if not inputValueCheck(money):
            return

        salary = int(money) * 12 * 10 ** 4
        tax_rate = calculate_tax(salary)
        tax = int(salary * tax_rate)
        after_tax_salary = salary - tax

        result = {
            '세전 연봉': f"{salary:,} 원",
            '세금 ': tax,
            '세후 연봉': f"{after_tax_salary:,} 원",
        }

        return result

    except ValueError:
        print("잘못된 결과입니다. FFFF")
        return

monthly_payment = input("월급을 입력하세요: ");
print(yearly_payment(monthly_payment))

#3.

def inputValueCheck(age, payment):
    if not age or not payment:
        print("나이 혹은 결제수단을 입력해주세요.")
        return False

    if (age.isdigit() == False):
        print("나이에 숫자만 들어있지 않습니다. 다시 입력하세요")
        return False
    if (payment.isalpha() == False):
        print("결제수단에 문자만 들어있지 않습니다. 다시 입력하세요")
        return False

    age = int(age)
    if(age < 0 or age>110):
        print("잘못된 나이입니다.")
        return False;
    return True


def solution(age, payment):
    try:
        if not inputValueCheck(age, payment):
            return
        result = {}

        age = int(age)
        prices = {
            "카드": {
                (0, 8): 0,
                (8, 14): 450,
                (14, 20): 720,
                (20, 75): 1200
            },
            "현금": {
                (0, 8): 450,
                (8, 14): 450,
                (14, 20): 1000,
                (20, 75): 1300
            }
        }

        if payment not in prices:
            print("올바르지 않은 결제 수단입니다.")
            return

        for (low, high), price in prices[payment].items():
            if low <= age < high:
                result = {
                    '나이': age,
                    '지불유형': payment,
                    '버스요금': price
                }

                print(f"나이: {age}")
                print(f"지불유형: {payment}")
                print(f"버스요금: {price}")
                return result
    except ValueError:
        print("잘못된 결과입니다. FFFF")
        return


age, payment = input("나이, 결제수단 입력하세요: ").split()
print(solution(age, payment))

#4.

import random

def inputValueCheck(myPick):
    if not myPick:
        print("가위바위보에 해당하는 문자 또는 숫자를 입력해주세요.")
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