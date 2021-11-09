import sys
import heapq as hq
# sys.stdin=open("input.txt", "r")
a=[]

ans=[];
#앞의 최소힙 코드에서 조금만 변경하면 됨.
#입력할 때 부호 바꿔버리면 됨.(그냥 입력 힙큐로 하면 최소힙이 디폴트라 최소힙으로 만듬)
#그럼 최대힙의 효과 내려몀ㄴ 입력시부호를 바꾼다 3,4 를 최대힙으로 만든다 치면
#-3,-4를 넣으면 -4가 최소라 위로 올라가고 여기서 -1을 또 곱하면 4 3 으로 최대힙 효과가 난다.
def solution():
    while True:
        n=int(input())
        if n==-1:
            break
        if n==0:
            if len(a)==0:
                # print(-1)
                return -1;
            else:
                # print(-hq.heappop(a))#원상태로 부호 바꿈.
                ans.append(-hq.heappop(a))
        else:
            hq.heappush(a, -n)#넣을떄 부호 반대로 바꿔서 넣음.
    return ans;
print(solution())

#앞의 최소힙 코드에서 조금만 변경하면 됨.
#입력할 때 부호 바꿔버리면 됨.(그냥 입력 힙큐로 하면 최소힙이 디폴트라 최소힙으로 만듬)
#그럼 최대힙의 효과 내려몀ㄴ 입력시부호를 바꾼다 3,4 를 최대힙으로 만든다 치면
#-3,-4를 넣으면 -4가 최소라 위로 올라가고 여기서 -1을 또 곱하면 4 3 으로 최대힙 효과가 난다.
