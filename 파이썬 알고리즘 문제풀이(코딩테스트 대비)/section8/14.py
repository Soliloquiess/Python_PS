import sys
from collections import deque
#sys.stdin=open("input.txt", "r")


n, m=map(int, input().split())
graph=[[0]*(n+1) for _ in range(n+1)]
degree=[0]*(n+1)
dQ=deque()

for i in range(m):
    a, b=map(int, input().split())
    graph[a][b]=1
    degree[b]+=1

for i in range(1, n+1):
    if degree[i]==0:
        dQ.append(i)

while dQ:
    x=dQ.popleft()
    print(x, end=' ')


    for i in range(1, n+1):
        if graph[x][i]==1:
            #x에서 i로 방향이 흐르는데 1이라면
            degree[i]-=1
            if degree[i]==0:
                dQ.append(i)

# degree 배열 만들어서 우선순위 넣어준다 0이면 먼저 처리해야할 일이 없어서 맨 앞,
# 1,2 이렇게 올라가면 먼저 처리해야 할 일들이 있어서 그럼 후처리
# 만약 0번이면 먼저 큐에 넣고 그다음 1번 우선순위 가진건 큐에넣고 이런식으로 하자.
# 그리고 큐에 있던 우선순위를 -1씩 해준다.
# 그리고 그 큐에 있던 우선순위가 0이 되면 큐에 넣어준다.
# 그리고 만약 5가 큐로 들어가면 0이 되는데 이 5의 진입차수 4로 들어가서 없애준다