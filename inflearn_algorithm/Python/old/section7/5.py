import sys
#sys.stdin = open("input.txt", 'r')
def DFS(L):
    global res
    if L==n:    #n이 되면 마지막 종착점에 온거
        cha=max(money)-min(money)   #최대값 최소값의 차
        #money에 3사람 금액 있는거
        if cha<res: #res가 기존 값인데 이거보다 작으면 답이 됨.
            #근데 머니에 있는 3개의 금액이 달라야함. (무조건 작다고 하는게 아니라 달라야됨)
            tmp=set()   #중복 제거 위한 set.
            for x in money:
                tmp.add(x)  #x가서로가 다 달랐다면 tmp 의 길이는 3이 됐을것.
            if len(tmp)==3: #tmp의 길이가 3일 떄 다 다른 금액.
                res=cha
    else:       #가지가 뻗어나가는 거
        for i in range(3):  #3명이니까 3번 돔 가지 뻗는다.
            money[i]+=coin[L]   #L번쨰 있는 돈을 i번쨰 사람한테 ㅈ줌
            DFS(L+1)        #다음 동전으로 감
            money[i]-=coin[L]   #여기로 왔다는건 전 상황으로 온거(전에 했던거 취소)
            #money[i]+=coin[L] 여기서 더했던 걸 뺴주는거( 전으로 돌아왔으므로)

if __name__=="__main__":
    n=int(input())  #동전 개수
    coin=[]         #각각 동전 코인이라는 리스트에 저장
    tmp=[]
    money=[0]*3     #0번사람, 1번사람 2번사람 각 사람의 극액
    res=2147000000  #res가 출력할 답
    for _ in range(n):  #포문 돌면서 코인이라는 리스트에 추가
        coin.append(int(input()))
    DFS(0)
    print(res)