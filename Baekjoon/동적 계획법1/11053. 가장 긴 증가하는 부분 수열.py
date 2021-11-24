n = int(input())
a = list(map(int, input().split()))
dp = [0 for i in range(n)]
for i in range(n):
    for j in range(i):
        if a[i] > a[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1
print(max(dp))


# https://pacific-ocean.tistory.com/153

# import sys
# #sys.stdin = open("input.txt", 'r')
# n=int(input())
# arr=list(map(int, input().split()))
# arr.insert(0,0)
#
# def solution(n,arr):
#     dy=[0]*(n+1)
#     dy[1]=1
#     res=0
#
#
#     for i in range(2, n+1): #맨 처음은 0,1로 되어있으므로 2부터 돌게한다.
#         max=0
#         for j in range(i-1, 0, -1):  #맨 뒤에서 앞으로 역순으로돈다.
#             if arr[j]<arr[i] and dy[j]>max:
#                 # arr[i]는 내가 만들고자 하는 증가수열의 마지막항
#                 # arr[j] 에서 j는 그 마지막 항의 앞의 항을 찾는거 j항이 작아야 앞의 항이 됨.
#                 # dy[j]는 arr[j]번쨰 있는 값이 마지막 항인 최대길이
#                 max=dy[j]   #arr[j]번쨰항이 마지막항이면서 최대길이  거기에 arr[i]가 들러붙어서 +1함
#         dy[i]=max+1 # 거기에 arr[i]가 들러붙어서 +1함
#
#         if dy[i]>res:
#             res=dy[i]   #다이나믹 테이블 중 가장 큰 값이 답임
#     # print(res)
#     return res;
# print(solution(n,arr));

# 맞는데 왜 안된다는지 도저히 몰겠네