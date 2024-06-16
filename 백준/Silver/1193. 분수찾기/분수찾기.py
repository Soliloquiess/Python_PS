# 입력 받기
X = int(input().strip())

# 대각선 번호와 그 번호까지의 총 원소 수를 찾기 위해 초기화
diagonal = 0
total_numbers = 0

# X가 포함될 대각선을 찾는다
while total_numbers < X:
    diagonal += 1
    total_numbers += diagonal

# 해당 대각선의 첫 번째 원소의 인덱스를 계산
previous_total = total_numbers - diagonal
index_in_diagonal = X - previous_total

# 대각선의 홀수/짝수에 따라 분자와 분모를 결정
if diagonal % 2 == 0:  # 사선 라인이 짝수번째 일 때
    numerator = index_in_diagonal
    denominator = diagonal - index_in_diagonal + 1
else: # 사선 라인이 홀수번째 일 때
    numerator = diagonal - index_in_diagonal + 1
    denominator = index_in_diagonal

# 결과 출력
print(f"{numerator}/{denominator}")


# input_num = int(input())
#
# line = 0  # 사선 라인
# max_num = 0  # 입력된 숫자(input_num 변수)의 라인에서 가장 큰 숫자
# while input_num > max_num:
#     line += 1
#     max_num += line
#
# gap = max_num - input_num
# if line % 2 == 0:  # 사선 라인이 짝수번째 일 때
#     top = line - gap  #분자
#     under = gap + 1  #분모
# else :  # 사선 라인이 홀수번째 일 때
#     top = gap + 1  #분자
#     under = line - gap  #분모
# print(f'{top}/{under}')