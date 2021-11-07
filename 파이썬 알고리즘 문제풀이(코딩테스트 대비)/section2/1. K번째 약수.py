import sys
#sys.stdin=open("input.txt", "r")
n, k=map(int, input().split())

def solution(n,k):
    cnt=0
    for i in range(1, n+1): #n까지 돌게
        if n%i==0:          #i가 n의 약수
            cnt+=1
        if cnt==k:          #k번쨰 약수 발견시
            return i;
            # print(i)        #그 약수는 i고 찾았으니까 출력.
            break
    else:                   #위가 참이 안되고 끝날수도(k번쨰 약수 못 찾았으므로.)
        print(-1)

print(solution(n,k));