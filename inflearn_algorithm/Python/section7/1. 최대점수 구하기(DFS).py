import sys
# sys.stdin=open("input.txt", "r")
def DFS(L, sum, time):
    global res
    if time>m:  #시간이 m이라는 제한시간 넘어가면 안됨. 넘어가면 바로 리턴
        return
    if L==n:    #문제 다 적용해서 부분집합 완성 된거
        if sum>res:     #문제 해서 얻는 점수가 res보다 크면
            res=sum     #res를 sum으로 바꿔줌.
    else:       #문제를 푸느냐 풀지 않느냐로 2갈래로 뻗음
        DFS(L+1, sum+pv[L], time+pt[L]) #L번쨰 문제 푸는거니까 sum에 점수 더해줌.

        #다음문제로 1 증가시킴(레벨(L) 1 증가)
        #pv의 l번쨰 문제 푼걸 점수에 더해주고
        #pt의 l번쨰 문제 푸는데 걸린 시간도 더해준다.
        # sum + pv[L]: 내가 얻은 점수
        # time + pt[L]: 내가 쓴 시간


        DFS(L+1, sum, time) #현재 문제 안푸는거 그냥 지나치고 다음문제 품.
    return res;
if __name__=="__main__":
    n, m=map(int, input().split())
    #n은 문제개수 m은 제한시간
    pv=list()   #문제 점수
    pt=list()   #문제 푸는데 걸리는 시간
    for i in range(n):  #포문 돌면서 a,b,에 점수, 시간 담음
        a, b=map(int, input().split())
        pv.append(a)
        pt.append(b)
    res=-2147000000#답이 될 거 최대값이니까  -정수 최소값 넣어줌.
    print(DFS(0, 0, 0))    #0번이 첫번쨰 문제 1번이 두번째문제
    print(res)
