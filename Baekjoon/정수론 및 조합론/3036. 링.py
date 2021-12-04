import sys
input = sys.stdin.readline

N = int(input()) # 링의 개수

li = list(map(int, input().split())) # 링 수

# 최대 공약수
def GCD(a,b) : # 항상 a 가 큰수
    while b!=0 :
        remain = a % b
        a = b
        b = remain

    return a

target = li.pop(0)

for i in range(N-1) :
    num = GCD(target, li[i])

    print('{}/{}'.format(target//num, li[i]//num))

#https://yongku.tistory.com/entry/%EB%B0%B1%EC%A4%80-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EB%B0%B1%EC%A4%80-3036%EB%B2%88-%ED%95%84%ED%84%B0-%ED%8C%8C%EC%9D%B4%EC%8D%ACPython