import sys
#sys.stdin=open("input.txt", "r")
n=int(input())
a=list(map(int, input().split()))   #a가 역수열임.
seq=[0]*n       #0으로 초기화된 1차원 리스트 필요. 그게 n개가 필요.
                #0번 인덱스부터 n-1까지 사용 가능.
#a.insert(0,0);
for i in range(n):      #0~n-1까지 돔. 근데 0이여도 1이라 생각하고 하는게 좋다.
    for j in range(n):  #위와 동일
    #for j in range(1,m+1):
        if(a[i]==0 and seq[j]==0):

                        #이 경우는 자기 자리 찾아 들어간 거.
                        #a에 i라는 숫자(a[i]값이)
                        #a[i]값이 자기 앞에 몇개가 있는지.
                        #a[i]==0이라는 의미는 자기앞에 자기보다 큰 숫자의 빈공간 다 만들어 낸거.
                        #seq[j] == 0는 j가 계속 돌고 있으니  그 j라는 곳이 찾아들어가더라도 빈자리여야 됨(숫자가 차 있으면 안됨.)
            seq[j]=i+1 #i가 0일때 1, 1일떄 2..(인덱스)
        #0됐단느 자기 앞에 빈공간 확보(자기보다 큰 숫자 들어가야 될)
        #자기보다 작은수가 자리 차지할 수 있으니까 들어가지 마라는 얘기(다음칸으로 가라j 증가해서)
        #i는 정렬된 자료 처리
        #1부터 하고 싶으면 for i in range(1,n)쓰자.

            break
        elif seq[j]==0: #0이면 빈 자리가 발견 된거고, 아직 자기 자리 찾아 들어가지 않음.
            a[i]-=1     #빈자리가 발견되면 i값을 하나 뺴줘라(빈자리를 하나 발견하면 i값이 하나 작아지니까 자기 앞이 비게
                        #예로 앞에 빈자리가 4개면 줄여서 0이 됐을떄 됨.
for x in seq:
    print(x, end=' ')