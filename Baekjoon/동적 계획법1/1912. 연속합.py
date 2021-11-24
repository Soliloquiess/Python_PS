n = int(input())

arr = list(map(int, input().split()))
dp = [0] * len(arr)
dp[0] = arr[0]

for i in range(1, len(arr)):
    dp[i] = max(arr[i], dp[i-1] + arr[i])

print(max(dp))

#https://kyoung-jnn.tistory.com/entry/%EB%B0%B1%EC%A4%801912%EB%B2%88%ED%8C%8C%EC%9D%B4%EC%8D%ACPython-%EC%97%B0%EC%86%8D-%ED%95%A9-DP

# 1912번 : 연속합
# n = int(input())
# a = list(map(int, input().split()))
#
# for i in range(1, n):
#     a[i] = max(a[i], a[i - 1] + a[i])
#
# print(max(a))

#https://wook-2124.tistory.com/406