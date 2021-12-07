import sys
#sys.stdin=open("input.txt", "r")
def Count(len):
    cnt=1       #처음에 말 한마리 배치
    #어디에? endpoint(ep)로 주고 말이 마지막에 배치된 지점이라고 둔다.
    ep=Line[0]   #첫번째 마굿간에 첫번째 말 배치
    for i in range(1, n):   #첫번째 부터 n-1까지
        if Line[i]-ep>=len: #라인의 i가 현재 내가 두번쨰 말을 배치해보려 하는거
            #마지막에 배치한지점 =ep 이값을 뻄. 그 거리가(Line[i]-ep) len보다 크면 라인 배치가능
            #현재 line[i]에 두번쨰, 세번쨰 말 이렇게 넣어가는거 거기에서 ep값 뺴는거
            #마지막에 말 배치한 지점과 현재 배치하려는 지점의 거리가 len보다 크면 우리가 말 배치 가능.
            cnt+=1
            ep=Line[i]  #카운트 한개 올렸으면 여기서 ep(해당 마구간 기준)을 바꿔준다.
    return cnt

n, c=map(int, input().split())
#n=마구간 좌표 개수 c= 말 배치(마릿수)
Line=[] #말 마구간의 좌표
def solution(n,c):
    for _ in range(n): #포문 돌면서 라인에 append
        tmp=int(input())
        Line.append(tmp)
    Line.sort() #마구간 좌표 정렬
    lt=1    #젤 작은 말의 최대 거리는 1
    rt=Line[n-1]    #마구간의 맨 끝 좌표고 이 사이들에 답이 있음.
    while lt<=rt:
        mid=(lt+rt)//2
        if Count(mid)>=c: #미드값 넘겼는데 mid값이 가장 가까운 거리 count는 말의 마릿수 배치
            #그게 참이 되면 mid는 답이 될 수 있음.
            res=mid #답을 찾으면 res에 mid값 넣음
            lt=mid+1    #답이 됐으면 그거보다 더 큰거리를 찾아본다.(최대거리 찾아야하므로)
        else:
            rt=mid-1    #더 큰값은 답이 안되므로 -1 답이 안되는 건 너무 길어서다. 그래서 줄여준다.

    # print(res)
    return res;
print(solution(n,c))


