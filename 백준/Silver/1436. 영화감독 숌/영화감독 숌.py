n = int(input().strip())

# 초기화
count = 0
number = 666

# 반복문을 사용하여 N번째 종말의 수를 찾습니다.
while True:
    if '666' in str(number):
        count += 1
        if count == n:
            print(number)
            break
    number += 1

# n = int(input())  # 입력값
# num = 666  # num은 666
# count = 0
#
# while True:
#     if "666" in str(num):  # num 문자열에 666이 있다면?
#         count += 1  # count + 1
#     if count == n:  # 더한 카운트와 입력값이 같다면 탈출
#         print(num)  # num 출력
#         break
#     num += 1  # num에 666이 없다면 1을 더한다.