input_data = input().split()
A = int(input_data[0])
B = int(input_data[1])

# 최대공약수(GCD) 구하기
a, b = A, B
while b != 0:
    a, b = b, a % b
gcd = a

# 최소공배수(LCM) 계산
lcm = (A * B) // gcd

# 최소공배수 출력
print(lcm)

# 
# # 입력 받기
# input_data = input().split()
# A = int(input_data[0])
# B = int(input_data[1])
# 
# # 최대공약수(GCD) 구하기
# def gcd(a, b):
#     while b != 0:
#         a, b = b, a % b
#     return a
# 
# # 최소공배수(LCM) 계산
# def lcm(a, b):
#     return (a * b) // gcd(a, b)
# 
# # 최소공배수 출력
# print(lcm(A, B))


# import sys
# import math
#
# input = sys.stdin.read
# data = input().split()
#
# A = int(data[0])
# B = int(data[1])
#
# # 최대공약수(GCD) 계산
# gcd = math.gcd(A, B)
#
# # 최소공배수(LCM) 계산
# lcm = A * B // gcd
#
# print(lcm)
