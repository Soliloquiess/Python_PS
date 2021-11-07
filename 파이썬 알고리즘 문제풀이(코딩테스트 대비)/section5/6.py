import sys
from collections import deque
#sys.stdin=open("input.txt", "r")
n, m=map(int, input().split())
Q=[(pos, val) for pos, val in enumerate(list(map(int, input().split())))]
#list ~끝까지 입력받는 부분
#enumerate 쓰면 키, 값 한번에 다 넣기 가능. [(0, 50) , (1,20)...]ㄴ이런식
Q=deque(Q)  #위에서 enumerate에서 키,값 한번에 넣는걸 덱으로 만들어준거.
cnt=0
while True:     #무한반복 하면서 n번째 사람이 진료 받는 순간 출력후 break.
    cur=Q.popleft()
    #(1,60)을 얘로 들면 cur[0]=1, cur[1]=60으로 들어온 거.
    if any(cur[1]<x[1] for x in Q):#value 값이 1번 `
        #for x in Q 포문이 돌면 Q에 자료를 x로 하나하나 접근함.
        #누구를 접근하냐면 50 70 90 90 이렇게 접근 x의 0번은 번째 1번은 위험도
        #cur[1]이랑 비교해서 위험도인 x[1]이 높으면 위험도가 더 높은 사람이다.

        #any라는 함수가 있는데 단하나라도 참이면 실행한다.
        #cur[1]<x[1] 이 식이 단 하나라도 참이면 이 사람은 진료 받으면 안됨.

        Q.append(cur)   #그대로 append시킴.
    else:
        #cur[1]<x[1] 이게 한개도 참이 아니면 진료 받아야(위험도 젤 높으므로)
        cnt+=1
        if cur[0]==m:   #현재 진료받는 사람이 cur인데 0이 번쨰 그게 m이면(m번쨰 사람 몇번쨰만에 진료받는지 찾는거니까)

            print(cnt)#출력.
            break
