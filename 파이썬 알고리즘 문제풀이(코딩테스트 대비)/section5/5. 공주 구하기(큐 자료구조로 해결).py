import sys
from collections import deque #덱 이용하기 위해 임포트해줌.
#sys.stdin=open("input.txt", "r")
n, k=map(int, input().split())
q=list(range(1, n+1))   #1부터 n+1까지(n이 8이면 1부터 8까지 생성됨.)
dq=deque(q)
def solution(n,k):
    while dq:
        for _ in range(k-1): #_는 빈 변수로 일단 만들어만 두겠다 의미 다 알지?
            cur=dq.popleft()
            dq.append(cur)  #k번쨰가 아니면 맨 왼쪽(앞)꺼 빼서 맨 오른쪽(뒤)에 넣겠다는 뜻.
        dq.popleft()    #k번째 되면 그 변수 팝하고 아예 덱에서 지워버림/.
        if len(dq)==1:  #만약 길이가 1이면 한개 남은거니까
            # print(dq[0])    #덱에 하나 남은거 출력하고
            return dq[0];
            dq.popleft()    #없애버리면 while문 나와버림/.

print(solution(n,k))