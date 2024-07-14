# 인자로 들어온 수의 제곱근까지만 확인하여 소수인지 아닌지를 검증하는 함수
# def isPrime(num):
#     if num == 1:
#         return False
#     else:
#         for n in range(2, int(num**0.5)+1):
#             if num % n == 0:
#                 return False
#         return True
#
# M, N = map(int, input().split())
#
# for i in range(M, N+1):
#     if isPrime(i):
#         print(i)


m, n = map(int, input().split())

def isprime(m, n):
  n += 1                            # for문 사용을 위한 n += 1
  prime = [True] * n                # n개의 [True]가 있는 리스트 생성
  for i in range(2, int(n**0.5)+1): # n의 제곱근까지만 검사 (n**0.5)를 계산하면 제곱근이 나온다. +1은 그 숫자까지 하기 위함.
    if prime[i]:                    # prime[i]가 True일때
      for j in range(2*i, n, i):    # prime 내 i의 배수들을 False로 변환
        prime[j] = False

  for i in range(m, n):
    if i > 1 and prime[i] == True:  # 1 이상이면서 남은 소수들을 출력
      print(i)

isprime(m, n)