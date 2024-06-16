import math
# 입력 받기
N = int(input().strip())

# N이 1보다 작거나 같으면 아무것도 출력하지 않음
if N <= 1:
    exit()

# 소인수분해할 때 필요한 변수 초기화
factors = []

# 2부터 N의 제곱근까지 반복하여 소인수를 찾음
for i in range(2, int(math.sqrt(N)) + 1):
    while (N % i) == 0:
        factors.append(i)
        N //= i

# N이 1보다 크면 마지막 소수인 경우이므로 추가해줌
if N > 1:
    factors.append(N)

# 소인수분해 결과 출력
for factor in factors:
    print(factor)
    
# n = int(input())
# 
# if n == 1:
#     print('')
# 
# # 2부터 하나씩 나눠보기
# for i in range(2, n + 1):
#     if n % i == 0:
#         # 해당 숫자로 나눌 수 없을 때까지 나누기
#         while n % i == 0:
#             print(i)
#             n = n / i

# import math
#
# num = int(input())
# 
# # 분해가 전부 될때까지 loop 돌립니다.
# while num != 1:
#     for i in range(2, num + 1):
#         # 나눠지면 출력하고,
#         # 다음을 위해 해당 수로 num을 나눠줍니다.
#         if(num % i == 0):
#             print(i)
#             num = num // i
#             break