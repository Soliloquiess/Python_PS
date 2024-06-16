n = int(input())

bee = 1  # 벌집의 개수, 1개부터 시작
cnt = 1
while n > bee :
    bee += 6 * cnt  # 벌집이 6의 배수로 증가
    cnt += 1  # 반복문을 반복하는 횟수
print(cnt)


# n = int(input())
#
# count =1;
# range =2;
#
# if(n==1):
#     print(1);
#
# else:
#     while(range<=n):
#         range = range+(6*count);
#         count+=1;
#
#     print(count)