def power(a, b):
    if b == 1: # b의 값이 1이면 a % C를 return한다.
        return a % C
    else:
        temp = power(a, b // 2) # a^(b // 2)를 미리 구한다.
        if b % 2 == 0:
            return temp * temp % C # b가 짝수인 경우
        else:
            return temp * temp * a % C # b가 홀수인 경우


if __name__ == "__main__":
    A, B, C = map(int, input().split())

    result = power(A, B)
    print(result)

# - 반복문으로 풀었는데, 시간초과가 났다.
# - 이 문제는 반복문으로 푸는게 아니라, 분할 정복(Divide And Conquer)으로 풀어야 한다.
# - 분할정복은 간단하다.
# - 예를 들어, 2^10은 2^5 * 2^5으로 나타낼 수 있다.(지수가 짝수일 경우)
# - 그리고, 2^11은 2^5 * 2^5 * 2로 나타낼 수 있다.(지수가 홀수일 경우)
# - 즉, 정해진 값을 절반으로 나눠서 계산하면 된다.

# import sys
#
# input = sys.stdin.readline
#
# # 값 입력
# A, B, C = map(int, input().split())
#
# # 분할 정복
# def DaC(a, b):
#     if b == 1:
#         return a % C
#
#     temp = DaC(a, b // 2)
#
#     # 짝수라면 temp * temp를 하면 된다.
#     if b % 2 == 0:
#         return temp * temp % C
#
#     # 홀수라면 temp * temp * a를 하면 된다.
#     else:
#         return temp * temp * a % C
#
#
# print(DaC(A, B))

# - 반복문으로 풀었는데, 시간초과가 났다.
# - 이 문제는 반복문으로 푸는게 아니라, 분할 정복(Divide And Conquer)으로 풀어야 한다.
# - 분할정복은 간단하다.
# - 예를 들어, 2^10은 2^5 * 2^5으로 나타낼 수 있다.(지수가 짝수일 경우)
# - 그리고, 2^11은 2^5 * 2^5 * 2로 나타낼 수 있다.(지수가 홀수일 경우)
# - 즉, 정해진 값을 절반으로 나눠서 계산하면 된다.