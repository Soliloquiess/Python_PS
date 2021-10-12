N, M = map(int,input().split())

arr = [[0]*7 for _ in range(2)]

for _ in range(N):
    S, Y = map(int,input().split())
    arr[S][Y] += 1

room = 0

for s in range(2):
    for y in range(1, 7):
        over = arr[s][y] // M # arr 값이 최대 인원을 넘는 경우, 몫
        rest = arr[s][y] % M # arr 값이 최대 인원을 넘는 경우, 나머지
        if arr[s][y]: # arr 값이 0 이상인 경우
            room += 1 # 기본적으로 방 갯수 추가
            if arr[s][y] > M: # arr 값이 최대 인원을 넘는 경우
                if rest: # 나머지가 있는 경우는
                    room += over # 몫 만큼 추가
                else: # 나머지가 0인 경우는
                    room += over - 1 # 몫-1 만큼 추가

print(room)