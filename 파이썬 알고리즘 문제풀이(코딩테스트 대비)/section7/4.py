import sys
#sys.stdin=open("input.txt", "r")
def DFS(L, sum):
    global cnt
    if sum>t:   #t금액이 넘어가면 컷해야됨(바로 리턴하자)
        #커트 안하면 시간초과 난다.
        return
    if L==k:    # k가 되면 말단노드까지 옴. 만약 20원 찾으면 20원 된거
        if sum==t:
            cnt+=1
    else:
        for i in range(cn[L]+1):    #0부터 cn까지 돌아야하므로 cn+1
            #cn[l]만큼 뻗음.
            DFS(L+1, sum+(cv[L]*i))
            # sum+(cv[L]*i)) 코인밸류cv에 [l]번쨰 여기에 곱하기 i해줌.
            # i가 1이면 1개 사용 , 2면 2개사용.

t=int(input())  #지폐의 개수
k=int(input())  #동전의 개수

cv=list()   #동전의 금액(coin value)
cn=list()   #동전의 개수(coin numbers)
for i in range(k):
    a, b=map(int, input().split())
    cv.append(a)#   0번에 첫 금액 5원 들어가고
    cn.append(b)#   0번에 5원의 개수인 3이 들어가는 거.
cnt=0
DFS(0, 0)
print(cnt)