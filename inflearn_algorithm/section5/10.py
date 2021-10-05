import sys
import heapq as hq  #힙큐 쓰기 위한 임포트
#sys.stdin=open("input.txt", "r")
a=[]
while True:
    n=int(input())  #숫자 하나 받음.
    if n==-1:       #-1이면 종료되는거.
        break
    if n==0:        #n이 0이면 힙에서 제일 루트노드에 있는거 찍어야.
        if len(a)==0:   #힙에 아무것도 없을 수 있으므로(리스트 길이가 0일떄)
            print(-1)   #-1출력
        else:           #그렇지 않으면
            print(hq.heappop(a))

            #루트노드에 제일 작은 값을 출력.힙큐라는 애를 쓰는데
            # 얘에서 제공하는 heappop이라는 애가 있는데 a에서 자료하나 뺴는데
            # 힙구조라면 루트노드값 뺴주는 거.


    else:   #0이 아니고 어떤 숫자니까 힙에 푸시해야되므로
        hq.heappush(a, n)   #a라는 리스트에 n을 푸시
        #트리형태로 (최소힙의 형태로) 넣음.


