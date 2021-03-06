import sys
#sys.stdin = open("input.txt", 'r')
dx=[-1, 0, 1, 0] #리스트 하나 생성.
dy=[0, 1, 0, -1] #i,j기준으로 -1,0은 위, 0,1 은 오른쪽 1,0은 아래, 0,-1은 왼쪽.(걍 행 열 어떻게 바뀌는지 보면 된다.)
n=int(input())
a=[list(map(int, input().split())) for _ in range(n)]
a.insert(0, [0]*n) #0번 행에다 n개의 0으로 초기화 된 행을 인서트 하라는 뜻 그니까 맨 위행에 [0 0 0 0 0]  이런식으로 들감..
a.append([0]*n) #마지막 밑부분에(n번행 쪽에) 넣음. 맨 밑쪽에 [0 0 0 0 0] 이렇게 넣음.
for x in a:     #for문이 돌면서 (x 가 2차원 리스트의 0번행 1번행.. 이렇게 감)
    x.insert(0, 0)  #젤 앞 열에다 삽임 그니까 0열 세로부분을 전부 0으로 초기화 하는거
    x.append(0)     #append해서 맨 끝에 추가(왼쪽과 오른쪽의 가장자리 열들을 다 0
    #여기까지하면 가장자리 상하좌우가 전부 0으로 초기화
cnt=0
for i in range(1, n+1):    #0번부터 돌면 안됨(0번은 가장자리이므로)
    for j in range(1, n+1):
        if all(a[i][j]>a[i+dx[k]][j+dy[k]] for k in range(4)):
            #파이썬에 all이라는 함수가 있는데 이 함수는 안의 조건이 모두 참일떄 참이 되는거
            #봉우리가 되려면 커야됨. k는 0부터3까지(4번)

            #a[i+dx[k]]가 행이고 [j+dy[k]]열
            #a[i+dx[k]][j+dy[k]]이렇게 돌면서 상하좌우 탐색.
            cnt+=1 #all이 참이면 봉우리이므로 +1을 해주면 됨.

print(cnt)