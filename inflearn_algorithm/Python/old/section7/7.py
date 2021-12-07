import sys
from collections import deque

#sys.stdin = open("input.txt", "r")
MAX = 10000
ch = [0] * (MAX + 1)
dis = [0] * (MAX + 1)
n, m = map(int, input().split()) #n이 출발점, m이 도착점
ch[n] = 1   #n에서 출발
dis[n] = 0  #출발점은 0
dQ = deque()
dQ.append(n)    #출발점에 추가
while dQ:       #큐는 비어있으면 멈춤
    now = dQ.popleft()  #맨 왼쪽 꺼냄.
    if now == m:    #now가 m값이 되면 도착(목표지점 도착)
        break       #그럼 멈추면 됨.
    for next in (now - 1, now + 1, now + 5):
        #3바퀴 돔 튜플값 하나하나 탐색
        if 0 <= next <= MAX:
            if ch[next] == 0:   #next가 이미 방문 했으면 넣어주면 안됨.
                #이게 0일떄만 next를 덱에 넣어줌
                dQ.append(next)
                ch[next] = 1    #그리고 방문했다라고 체크 검.
                dis[next] = dis[now] + 1    #dis는 next는 자기 부모값(자기 부모가 now)
                #나우에서 하나 뻗었으니까 +1해줌

print(dis[m])#도착지점(출발지점에서 m으로 가는데 얼마나 걸리나)