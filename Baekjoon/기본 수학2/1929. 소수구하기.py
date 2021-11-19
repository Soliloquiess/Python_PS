import math

def isPrime(num):
    if num == 1: return False

    n = int(math.sqrt(num))
    for k in range(2, n+1):
        if num % k == 0:
            return False
    return True

# main
m, n = map(int, input().split())
for k in range(m, n+1):
    if isPrime(k):
        print(k)
# 2부터 k의 제곱근까지 확인한다. 만약 나누어떨어진다면 그 숫자는 소수가 아니다. 나누어 떨어진다는 것은 다른 약수를 가진다는 뜻.
# https://hongku.tistory.com/274




# M, N = map(int, input().split())
#
# def prime_sieve(M, N):
#     N += 1
#     sieve = [True] * N
#     for i in range(2, int(N**0.5)+1):
#     for i in range(2, int(math.sqrt(N)) + 1): 이렇게 써도 바로 윗 줄과 동일.

#         if sieve[i]:
#             for j in range(2*i, N, i):
#                 sieve[j] = False
#     for i in range(M, N):
#         if i > 1:
#             if sieve[i]:
#                 print(i)
#
# prime_sieve(M, N)
#https://wlstyql.tistory.com/73?category=852442