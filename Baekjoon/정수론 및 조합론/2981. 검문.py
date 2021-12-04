# 최대공약수를 빠르게 구해주는 유클리드 호제법
def gcd(x, y):
    mod = x % y
    while mod > 0:
        x = y
        y = mod
        mod = x % y
    return y


# 약수 리스트를 구해주는 함수
def div(x):
    div_list = [x]
    for i in range(2, int(x ** (1 / 2) + 1)):
        if x % i == 0:
            div_list.append(i)
            if x // i != i:
                div_list.append(x // i)
    div_list.sort()
    return div_list


# 입력함수
N = int(input())
freight = []
for _ in range(N):
    freight.append(int(input()))
freight.sort(reverse=True)

# 화물들의 차이 입력
freight_diff = []
for i in range(len(freight) - 1):
    freight_diff.append(freight[i] - freight[i + 1])

# 화물들의 차이를 최대공약수 함수를 이용해 구해주기
if len(freight_diff) == 1:
    answer = freight_diff[0]
elif len(freight_diff) == 2:
    answer = gcd(freight_diff[0], freight_diff[1])
else:
    answer = freight_diff[0]
    for i in range(1, len(freight_diff)):
        answer = gcd(answer, freight_diff[i])

    # 구한 최대공약수의 모든 약수 출력
for i in div(answer):
    print(i, end=' ')
#https://claude-u.tistory.com/260

#2981

#최대 공약수 구하는 함수
# def gcd(a, b):
#     while b:
#         a, b = b, a%b
#     return a
#
# n = int(input())
# ls = []
#
# for i in range(n):
#     ls.append(int(input()))
# min_n = min(ls) #최솟값 구하기
#
# for i in range(len(ls)):
#     if ls[i] > min_n:
#         ls[i] = ls[i] - min_n #모든 자연수를 최솟값으로 빼주기
# ls.remove(min_n) #최솟값은 원래 리스트에서 제거
#
# #위에서 계산한 자연수-최솟값들 모두의 최대 공약수 구하기
# gcd_n = ls[0]
# for i in range(len(ls)):
#     gcd_n = gcd(gcd_n, ls[i])
#
# #최대 공약수의 약수 구하기
# for i in range(2, gcd_n+1):
#     if gcd_n%i==0:
#         print(i,end = ' ')
#https://skyjwoo.tistory.com/entry/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EB%B0%B1%EC%A4%80-ATM-11399-%EA%B2%80%EB%AC%B8-2981

# from math import gcd
# from math import sqrt
#
# n = int(input())
# ns = list(int(input()) for _ in range(n))
# ns.sort()
# interval = list()
# ans = list()
#
# for i in range(1, n):
#     interval.append(ns[i] - ns[i - 1])
#
# prev = interval[0]
# for i in range(1, len(interval)):
#     prev = gcd(prev, interval[i])
#
# for i in range(2, int(sqrt(prev)) + 1): #제곱근까지만 탐색
#     if prev % i == 0:
#         ans.append(i)
#         ans.append(prev//i)
# ans.append(prev)
# ans = list(set(ans)) #중복이 있을수 있으니 제거
# ans.sort()
# print(*ans)

# https://tmdrl5779.tistory.com/94