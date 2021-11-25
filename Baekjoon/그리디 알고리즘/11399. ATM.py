n = int(input())
s = list(map(int, input().split()))
num = 0
s.sort()
for i in range(n):
    for j in range(i + 1):
        num += s[j]
print(num)

# https://pacific-ocean.tistory.com/227

# n = int(input()) # 사람 수
# arr = list(map(int,input().split())) # 인출 시간
# arr.sort() # 정렬
#
# result = 0
#
# for i in range(1,n):
#     arr[i] += arr[i-1] # 인출 시간 갱신
#
# print(sum(arr))

#https://deep-learning-study.tistory.com/629