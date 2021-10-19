# def solution(n):
#     answer = ''
#
#     while n > 0:
#         n, re = divmod(n,3)	# n을 3으로 나눈 몫과 나머지
#         answer += str(re) #3으로 나눈 나머지를 answer에 더해준다.
#     return int(answer, 3) #이러면 그냥 3진법으로 바꿔준다.. 머선
#
# # divmod() : 몫과 나머지를 리턴합니다. 리턴 값이 2개이므로 튜플을 사용합니다.
# # int(x, base) : base 진법으로 구성된 str 형식의 수를 10진법으로 변환해 줌
# print(solution(113))

def solution(n):
    answer = ''
    result = 0

    while n >= 1:
        rest = n % 3
        n //= 3
        answer += str(rest)

    i = 0
    for idx in range(len(answer)-1, -1, -1):
        result += int(answer[idx]) * (3**i)
        i += 1

    return result

print(solution(113))