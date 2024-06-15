# 입력 받기
N, B = input().split()
N = int(N)
B = int(B)

# 결과를 저장할 문자열
result = ""

# 변환 과정
while N > 0:
    remainder = N % B
    if remainder >= 10:
        # 10 이상인 경우 문자로 변환
        result = chr(remainder - 10 + ord('A')) + result
    else:
        # 10 미만인 경우 숫자로 변환
        result = str(remainder) + result
    N = N // B

# 결과 출력
print(result)


# # 입력 받기
# N, B = input().split()
# N = int(N)
# B = int(B)
# 
# # 진법 변환에 필요한 문자 리스트
# digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# 
# #digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ" 문자열은 주어진 숫자를
# # 다양한 진법으로 변환할 때 사용될 수 있는 숫자와 문자들을 모두 포함하고 있다.
# # 예를 들어, 2진법부터 36진법까지의 숫자를 나타낼 때, 각 자리 숫자는 0부터 9,
# # 그리고 A부터 Z까지의 문자로 표현
# 
# # 결과를 저장할 문자열
# result = ""
# 
# # 변환 과정
# while N > 0:
#     remainder = N % B
#     result = digits[remainder] + result
#     N = N // B
# 
# # 결과 출력
# print(result)