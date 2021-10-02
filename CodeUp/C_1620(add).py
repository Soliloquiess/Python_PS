def solution(n):
    answer=0
    while n>0 :
        answer+=n%10
        n//=10
    return answer

result = solution(int(input()));

print(result);

# def sum_digit(number):
#     '''number의 각 자릿수를 더해서 return하세요'''
#     num = str(number)
#     sum = 0
#     for i in range(len(num)):
#         sum += int(num[i])
#     return sum
#
# # 아래는 테스트로 출력해 보기 위한 코드입니다.
# print("결과 : {}".format(sum_digit(123)));