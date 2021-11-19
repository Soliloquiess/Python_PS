def sosu(n):
    if n ==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True							#소수 구하는 방식은 위와 같다

all_list = list(range(2,246912))		#문제에서 제한한 범위
memo = []								#for문 밖에 리스트 정의

for i in all_list:						#2부터 2*123,456 범위
    if sosu(i):							#sosu함수에 해당하면
        memo.append(i)					#리스트에 추가

n = int(input())

while True:
    count=0					#갯수를 세야하는 조건 때문에 카운트
    if n == 0 :
            break
    for i in memo:			#memo리스트 중에서
        if n < i <=2*n:		#입력한 값의 범위 내에서 값이 있으면
            count+=1		#있을 때 마다 카운트 +1
    print(count)
    n = int(input())		#0 입력받기 전까지 계속 해야하므로 입력 받음


#시간초과 코드
# def sosu(x):
#     if x ==1:            #1은 모든 수의 약수이기 때문에 pass
#         return False
#     for i in range(2,int(x**0.5)+1):  #제곱근이 있는 수 중에
#         if x%i==0:					#약수가 있으면 false	
#             return False
#     return True						#이외에는 소수
# 
# 
# 
# while True:
#     n = int(input())				#범위를 주기 위한 입력
#     count=0
#     if n == 0 :						#0 입력하면 아웃되는 게 조건
#             break
#     for i in range(n,2*n+1):		#n과 2n+1사이에서
#         if sosu(i):					#sosu함수안에 있는 게 있다면
#             count+=1					#카운트를 세라
#     print(count)		#개수를 출력하는 조건에 맞춰 카운트를 출력
#시간초과


# import sys
# import math
#
# limit = 123456
# #문제에 123456 이하의 숫자가 입력 될 것이라고 했으므로, limit를 123456으로 설정했다.
#
#
# eratos = [1] * (2 * limit + 1) #n부터 2n까지 계산을 해야하므로 limit의 2배 길이 리스트를 미리 생성하고 전부 1로 초기화했다.
# #+1을 더해준 이유는 인덱스번호가 0부터 시작하기때문에 편의상 인덱스 번호와 실제 숫자를 맞춰주기 위함이다.
# eratos[0] = 0
# eratos[1] = 0
# #0과 1은 소수가 아니므로 미리 0으로 체크해준다.
#
#
# for i in range(2, int(math.sqrt(len(eratos)))):
#     if eratos[i]:
#         for j in range(i + i, len(eratos), i):
#             eratos[j] = 0
#
# while True:
#     n = int(sys.stdin.readline())
#     if n == 0:
#         break
#     else:
#         print(sum(eratos[n + 1:(2 * n) + 1]))   #미리 구해놓은 리스트에서 n보다 크고 2n보다 작거나 같은 소수의 갯수를 구해 출력한다.
#
# # https://itholic.github.io/kata-bertrands-postulate/
#
#
#
#
