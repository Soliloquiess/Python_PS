# N, M, K를 공백을 기준으로 구분하여 입력 받기
n, m, k = map(int, input().split())
# N개의 수를 공백을 기준으로 구분하여 입력 받기
data = list(map(int, input().split()))

data.sort() # 입력 받은 수들 정렬하기
first = data[n - 1] # 가장 큰 수
second = data[n - 2] # 두 번째로 큰 수

result = 0;

# 가장 큰 수가 더해지는 횟수 계산
#근데 이렇게 알고리즘 짜면 1억, 100억개가 들어오면 시간초과가 난다.
# while True:
# 	for i in range(k): #가장 큰 수 더하기
# 		if m ==0: #m이 0이라면 반복문 탈출
# 			break;
# 		result+=first;
# 		m-=1; #더할때 마다 1 뺴기
#
# 	if m ==0:	#m이 0이면 탈출
# 		break;
#
# 	result +=second; #두번째로 큰 수 더하기
# 	m-=1;	#더할때마다 1 빼기
# print(result);

# 가장 큰 수가 더해지는 횟수 계산

count = int(m / (k + 1)) * k	#수열 형식의 규칙이 이 과정에서 나온다.
count += m % (k + 1)

result = 0
result += (count) * first # 가장 큰 수 더하기
result += (m - count) * second # 두 번째로 큰 수 더하기

print(result) # 최종 답안 출력