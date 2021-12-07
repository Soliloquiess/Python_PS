import sys
#sys.stdin = open("input.txt", 'r')

#dis[5][4]= dis[5][3] + dis[3][4]

#dy[i][j]는 i에서 j로 가는데 드는 비용
if __name__=="__main__":
    n, m=map(int, input().split())  #m은 5000으로 가장 큰 값 줌(초기화)
    dis=[[5000]*(n+1) for _ in range(n+1)]



    for i in range(1, n+1): # 이 포문은 i i 다 맥스로 초기화
        dis[i][i]=0         # 자기자신으로 가는건 다 0으로 초기화

    for i in range(m):    # 인접행렬 만드는 포문
        a, b, c=map(int, input().split())   # 여기서 최초로 dis라는 테이블 초기화 됨
        dis[a][b]=c         # 이 포문 돌고난 뒤 dis테이블의 초기화는 i에서 j로 가는데 중간에 전혀 아무 노드도 거치지 않고 바로 직행하는

        # 그 떄 최소값들이 초기화 됨(직행 했을떄) 한번에 갈수 없으면 5000 그대로 있겠지.
        # 아무튼 이 포문은 i에서 j로 가는데 드는 최소비용 들가있음



    #이 3중포문이 플로이드 워셜 알고리즘
    for k in range(1, n+1): # 가운데 노드
        for i in range(1, n+1): # //시작 노드
            for j in range(1, n+1): #  //마지막 노드
                dis[i][j]=min(dis[i][j], dis[i][k]+dis[k][j]) #이 3중포문이 플루워드 워셜

                # //가운데를 거쳐가는 것이 더 빠르면 그걸로 업데이트한다.
                #dis[i][k]+dis[k][j] 이 부분이 k를 거쳐서 간다고 가정하는 부분
                #i에서 k를 거쳐서 간다고 가정했을떄 부분이게 기존값보다 작으면 바꿔줌.(냅색 알고리즘과 유사)
                #이게 n까지 돌면 다 적용 된거

                #이 dis에는 최상위 값으로 다이나믹 테이블이 완성됨


    for i in range(1, n+1):   #이 포문은 그냥 2중 포문의 출력(2중 포문으로 dis 배열 다 출력)
        for j in range(1, n+1):
            if dis[i][j]==5000:
                print("M", end=' ')
            else:
                print(dis[i][j], end=' ')
        print()
# https://namu.wiki/w/%ED%94%8C%EB%A1%9C%EC%9D%B4%EB%93%9C-%EC%9B%8C%EC%85%9C%20%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98

#플로이드 와샬은 모든정점에서 모든정점으로 가는 알고리즘
#여기서 최단거리를 구하는 문제
#다이나믹 테이블은 2차원이다.

#참고로 순서는 꼭 0,0이 1번노드가 아니고 i->j i->k->j이렇게 가는데
# 1->2 만 아니라 2->1도 갈수 가 있는 거