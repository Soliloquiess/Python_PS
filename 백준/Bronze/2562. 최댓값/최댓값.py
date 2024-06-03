# 입력 받기
numbers = [int(input()) for _ in 9]

# 초기 최댓값 설정
max_value = numbers[0]
max_index = 1

# 최댓값과 그 인덱스 찾기
for i in range(1, 9):
    if numbers[i] > max_value:
        max_value = numbers[i]
        max_index = i + 1  # 인덱스는 1부터 시작

# 결과 출력
print(max_value)
print(max_index)


# List =[];
# max=0;
# max_index=0;
# for i in range(9):
#     i = int(input())
#     List.append(i)
# 
# 
# for i in range(0,9):
#     if(List[i] > max):
#         max= List[i];
#         max_index=i+1;
# print(max,sep="");
# print(max_index);
