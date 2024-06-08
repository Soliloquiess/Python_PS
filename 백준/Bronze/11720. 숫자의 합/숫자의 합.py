m=input();
n=input()

arr = list(n)
sum =0;
arr= list(map(int, arr));

for i in range(len(n)):
    sum += arr[i];

print(sum)


# # Step 1: 입력 받기
# N = int(input().strip())  # 첫 번째 입력값: 숫자의 개수 N
# numbers = input().strip()  # 두 번째 입력값: 공백 없이 이어진 숫자들
# 
# # Step 2: 숫자들을 모두 더하기
# total_sum = sum(int(num) for num in numbers)
# 
# # Step 3: 결과 출력
# print(total_sum)
