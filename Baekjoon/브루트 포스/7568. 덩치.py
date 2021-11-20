N = int(input())

people = []
for _ in range(N):
    w, h = map(int, input().split())
    people.append((w, h))

for c in people:  # 0
    rank = 1  # 1

    for n in people:    #c하나 잡고 n 돌면서 확인
        if (c[0] != n[0]) & (c[1] != n[1]):  # 2
            if (c[0] < n[0]) & (c[1] < n[1]):  # 3 w, h 모두 큰 경우
                rank += 1

    print(rank)

#0 : c는 현재 사람, n은 다음 사람
#1 : 나보다 덩치 큰 사람 수 + 1
#2 : 자신을 제외하고 비교
#3 : c[0], n[0]은 몸무게, c[1], n[1]은 키