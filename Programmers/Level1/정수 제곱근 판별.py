import math
def solution(n):
    a=math.sqrt(n)
    if int(a)==a:
        return (a+1)**2
    else:
        return -1
print(solution(121))

# def solution(n):
#     a=n**0.5
#     if int(a)==a:
#         return (a+1)**2
#     else:
#         return -1
# print(solution(121))

# import math
#
# def solution(n):
#     if n % math.sqrt(n) == 0:
#         return math.pow(math.sqrt(n)+1,2)   #pow는 거듭제곱해주는 함수
#     return -1