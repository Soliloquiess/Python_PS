n = int(input())

li = [1, 2]

for i in range(2, n):
    li.append((li[i - 1] + li[i - 2]) % 15746)
print(li[n - 1])

# https://jiwon-coding.tistory.com/30?category=882771


# import sys
# input = sys.stdin.readline
#
# n = int(input())
# dp = [0] * 1000001
# dp[1] = 1
# dp[2] = 2
#
# for k in range(3,n+1):
#     dp[k] = (dp[k-1]+ dp[k-2])%15746
# print(dp[n])

#https://sungmin-joo.tistory.com/21

