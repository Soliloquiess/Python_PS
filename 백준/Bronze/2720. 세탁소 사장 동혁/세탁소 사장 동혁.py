# 테스트 케이스의 수를 입력 받음
T = int(input())

# 각 테스트 케이스에 대해 처리
for _ in range(T):
    # 거스름돈을 센트 단위로 입력 받음
    C = int(input())

    # 동전의 가치를 상수로 정의
    QUARTER = 25
    DIME = 10
    NICKEL = 5
    PENNY = 1

    # 각 동전의 개수를 계산
    quarters = C // QUARTER
    C %= QUARTER

    dimes = C // DIME
    C %= DIME

    nickels = C // NICKEL
    C %= NICKEL

    pennies = C // PENNY

    # 결과 출력
    print(quarters, dimes, nickels, pennies)

# 함수 쓰면

# def calculate_change(cents):
#     # 동전의 가치를 상수로 정의
#     QUARTER = 25
#     DIME = 10
#     NICKEL = 5
#     PENNY = 1
#
#     # 각 동전의 개수를 계산
#     quarters = cents // QUARTER
#     cents %= QUARTER
#
#     dimes = cents // DIME
#     cents %= DIME
#
#     nickels = cents // NICKEL
#     cents %= NICKEL
#
#     pennies = cents // PENNY
#
#     return quarters, dimes, nickels, pennies
#
#
# # 테스트 케이스의 수를 입력 받음
# T = int(input())
#
# # 각 테스트 케이스에 대해 거스름돈을 입력 받고 결과를 출력
# for _ in range(T):
#     C = int(input())
#     quarters, dimes, nickels, pennies = calculate_change(C)
#     print(quarters, dimes, nickels, pennies)
