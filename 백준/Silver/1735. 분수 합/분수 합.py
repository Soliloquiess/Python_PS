import math

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def add_fractions(n1, d1, n2, d2):
    # 공통 분모를 구하기 위해 두 분모의 곱을 사용
    common_denominator = d1 * d2
    # 분자 변환
    numerator1 = n1 * d2
    numerator2 = n2 * d1
    # 두 분자의 합
    numerator_sum = numerator1 + numerator2
    # 기약분수를 만들기 위해 GCD 구하기
    common_gcd = gcd(numerator_sum, common_denominator)
    # 분자와 분모를 GCD로 나누기
    final_numerator = numerator_sum // common_gcd
    final_denominator = common_denominator // common_gcd
    return final_numerator, final_denominator

# 입력 받기
n1, d1 = map(int, input().split())
n2, d2 = map(int, input().split())

# 분수 합 구하기
final_numerator, final_denominator = add_fractions(n1, d1, n2, d2)

# 결과 출력
print(final_numerator, final_denominator)
