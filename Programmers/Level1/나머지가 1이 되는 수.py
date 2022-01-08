import math

def solution(n):
    x = n - 1 #나머지 먼저계산
    if x % 2 == 0:
        return 2
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return i
    return x
# n을 x로 나눈 나머지가 1이 되는 x의 수 중 가장 큰 수 x = n - 1
# x 가 짝수면 2 return
# x가 소수인지 판별하는 과정에서 약수 발견 시 가장 작은 약수 return, x가 소수이면 x return

print(solution(10))

# def solution(n):
#
#     if not 3 <= n <= 1000000 :
#         return False
#
#     answer = 2    #맨 첫값이 3이라 3%2=1이라 디폴트 앤서가 2다.
#     while True :
#         if n % answer == 1 :
#             break
#         else :
#             answer += 1
#
#     return answer

# print(solution(10))
