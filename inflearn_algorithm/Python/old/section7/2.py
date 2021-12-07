import sys
#sys.stdin=open("input.txt", "r")
def DFS(L, sum):    #L이 진행되어가는 날짜
    global res
    if L==n+1:      #종료지점은 n+1
        if sum>res:
            res=sum #sum이 더 크면 갱신
    else:
        if L+T[L]<=n+1: #L번쨰 상담한다 했을때 L이 현재지점인데 T[L]이 앞으로 상담할 날짜(걸리는 날짜)가 n+1을 넘으면 안됨
            #그래야 가지 뻗어나감.
            # T의 L번쨰 날에 상담하는거 앞으로 상담할 날짜를 더해주고 n+1을 넘으면 안된다.

            DFS(L+T[L], sum+P[L])
             #이 else부분은 L이란 날짜에 잡힌 상담을 하는거 현재 날짜에 그 날짜에 잡힌 상담 더해주는거 그리고 다음 상담 가는거(누적
            #L+T[L]<=n+1 이부분은 다음에 해야될 지점으로 갈 날짜가  현재 상담 더해줌.(걸리는 시간)
            #그게 n+1보다 작거나 같아야만 가지 뻗어감. 그리고 종료지점은 꼭 n+1이여야됨.
       
       
        DFS(L+1, sum)#상담을 하지 않으면 그냥 레벨만 증가(다음말짜)

if __name__=="__main__":
    n=int(input())  #날짜(7일)
    T=list()    #걸리는 시간
    P=list()    #얻을수 있는 금액.
    for i in range(n):
        a, b=map(int, input().split())
        T.append(a)
        P.append(b)
    res=-2147000000

    T.insert(0, 0)
    P.insert(0, 0)
    # 이렇게 하면 미는 효과 일어남, 4, 20을 맨 앞 인덱스 0, 0에 들어가니까
    # 0,0인덱스에 0, 0의미없는 숫자 넣고 인덱스 맞추기 위해 인덱스 1 부터 4, 20을 각 T,P에 넣음.



    DFS(1, 0)
    print(res)

#N+1이 종료지점(휴가 떠나는 날) 7일에서시작 8일쨰 종료는 가능한데 n+2,N+3..이상 은 안된다