import math

def is_prime(x):
    """주어진 숫자 x가 소수인지 확인하는 함수"""
    if x < 2:
        return False
    if x in (2, 3):
        return True
    if x % 2 == 0 or x % 3 == 0:
        return False
    i = 5
    while i * i <= x:
        if x % i == 0 or x % (i + 2) == 0:
            return False
        i += 6
    return True

def next_prime(n):
    """주어진 숫자 n보다 크거나 같은 소수 중 가장 작은 소수를 찾는 함수"""
    if n <= 2:
        return 2
    if n % 2 == 0: # 짝수니까 최소한 홀수 만들려고 +1 시킴.
        n += 1
    while not is_prime(n): #홀수에서 다음 홀수 찾으라고 +=1 시킨거
        n += 2
    return n

# 입력 처리
num_cases = int(input())
results = []

for _ in range(num_cases):
    n = int(input())
    results.append(next_prime(n))

# 출력 처리
for result in results:
    print(result)
