# 1010번

def factorial(n):
    num = 1
    for i in range(1, n+1):
        num *= i
    return num


T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    bridge = factorial(m) // (factorial(n) * factorial(m - n))
    print(bridge)


# 1010번

# import math
#
# T = int(input())
#
# for _ in range(T):
#     n, m = map(int, input().split())
#     bridge = math.factorial(m) // (math.factorial(n) * math.factorial(m - n))
#     print(bridge)
#https://yoonsang-it.tistory.com/33