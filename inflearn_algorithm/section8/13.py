import sys
#sys.stdin = open("input.txt", 'r')


if __name__=="__main__":
    n=int(input())
    dis=[[100]*(n+1) for _ in range(n+1)]   #dis 테이블에 플로이드 워셜 사용할 것


    for i in range(1, n+1): #dis 자기자신을 0으로 한거
        dis[i][i]=0

    # dis 라는 인접행렬을 초기화 했다.
    while True:
        a, b=map(int, input().split())
        if a==-1 and b==-1:
            break
        dis[a][b]=1
        dis[b][a]=1 #무방향 그래프니까(친구사이니까)
    
    #플로이드 워셜
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                dis[i][j]=min(dis[i][j], dis[i][k]+dis[k][j])   #앞 문제에서의 플로이드 워셜
                #이렇게 하면 dis테이블이 가까움의 정도를 다 구함


    res=[0]*(n+1)   #res라는 리스트 만듬.
    score=100


    #2중포문 돌면서 각 회원 정보를 res에 넣는다.
    for i in range(1, n+1): #n까지 돌아야
        for j in range(1, n+1): #n까지 돌아야
            res[i]=max(res[i], dis[i][j])   #res의 i에 i번 회원의 최대값을 기록하는거
        score=min(score, res[i])   #기존 res값보다 res[i가 더 작으면 스코어에 넣어줌]
        #제일 작은값이 score로 기록됨. 이 스코어가 회장 후보가 될 수 있는 점수
    #i번 회원의 최대값을 res에 저장. dis[i][j]가 각 회원간들의 가까운 정도이다.

    out=[]  #이 리스트에 회장 후보 될 수 있는 사람 번호 넣음


    for i in range(1, n+1):
        if res[i]==score:   #회장후보가 될 수 있는 점수 가진 사람을 out에 넣음.
            out.append(i)

    print("%d %d" %(score, len(out)))   #이건 추가된 회원후보 수(몇 명인지)

    for x in out:
        print(x, end=' ')