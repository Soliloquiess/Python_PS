# # 입력 받기
# input_data = input().strip().split()
#
# # N과 K 추출
# N = int(input_data[0])
# K = int(input_data[1])
#

# 입력 받기
N, K = list(map(int, input().split()))

# 약수 구하기
divisors = []
for i in range(1, N+1):
    if N % i == 0:
        divisors.append(i)

# K번째 약수 찾기
if K <= len(divisors):
    result = divisors[K-1]
else:
    result = 0

# 결과 출력
print(result)
