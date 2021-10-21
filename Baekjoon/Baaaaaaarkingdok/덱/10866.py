import sys
from collections import deque

input = sys.stdin.readline

N = int(input())  # 명령의 수

dq = deque()

for _ in range(N):
    Order = list(input().split())

    if Order[0] == "push_front":
        dq.appendleft(Order[1])

    elif Order[0] == "push_back":
        dq.append(Order[1])

    elif Order[0] == "pop_front":
        if len(dq) == 0:
            print(-1)
        else:
            print(dq.popleft())

    elif Order[0] == "pop_back":
        if len(dq) == 0:
            print(-1)

        else:
            print(dq.pop())

    elif Order[0] == "size":
        print(len(dq))

    elif Order[0] == "empty":
        if len(dq) == 0:
            print(1)
        else:
            print(0)

    elif Order[0] == "front":
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[0])

    elif Order[0] == "back":
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[-1])

# - deque 라이브러리를 사용하여 문제를 풀 수 있다.

# - 물론, 리스트로 구현하여 push와 pop을 해도 상관은 없다.