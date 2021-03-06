import sys
#sys.stdin = open("input.txt", 'r')
#dy[i][j] 는 i,j까지 가는 최소 비용
if __name__=="__main__":
    n=int(input())

    arr=[list(map(int, input().split())) for _ in range(n)]
    dy=[[0]*n for _ in range(n)]
    dy[0][0]=arr[0][0]  #첫번쨰 돌 하나 받는게 최소비용

    for i in range(1, n):
        dy[0][i]=dy[0][i-1]+arr[0][i]   #dy[0][i-1] 이게 자기 왼쪽까지 다이나믹값(바로 왼쪽 앞에까지 오는데) 최소비용
        #0행부터 도는거(자기 왼편까지 다이나믹행)  자기 바로 왼쪽까지 오는거에 자기 번호의 열
        #자기 돌을 더해줌 arr[0][i]
        dy[i][0]=dy[i-1][0]+arr[i][0]   #dy[i-1][0] 여기도 자기 바로 위에까지 오는데 비용 + 자기 돌을 더해줌 arr[0][i]
        #0열 자기 바로 위에까지 오는데 비용 + 자기 열

    for i in range(1, n):   #1~n까지 돈다.
        for j in range(1, n):   #1행 1열부터 돔
            dy[i][j]=min(dy[i-1][j], dy[i][j-1])+arr[i][j]  #이 둘중 작은값 받아야(dy[i-1][j]:자기 바로 왼쪽까지 오는데 최소비용 ,dy[i][j-1]:자기 바로 위쪽까지 오는데 최소비용 중)
            #거기에 자기 돌을 밟아야 되는 비용 arr[i][j](i,j 에 있는 돌 밟는 거 더해주는거)

    print(dy[n-1][n-1])	#0,0 에서 잡았으니까 n-1 ,n-1이 답

#dy[i][j]= 최소비용