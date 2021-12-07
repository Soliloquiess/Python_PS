import sys

# sys.stdin = open("input.txt", 'r')
n = int(input())  # 벽돌의개수
bricks = []  # 이 리스트에 벽돌 정보 넣을거.
def solution(n,bricks):
    for i in range(n):
        a, b, c = map(int, input().split())
        bricks.append((a, b, c))  # 튜플형태로 넣음
    bricks.sort(reverse=True)  # 역순 정렬(내림차순)
    # 이 경우 a를 기준으로(맨 처음 입력된 요소) 정렬을 한다.
    # 이 경우엔 a를 기준으로 내림차순 정렬

    dy = [0] * n
    dy[0] = bricks[0][1]  # 0번 벽돌이 1개만 있었을 떄의 그 높이

    # bricks[0][1] 에서 brick의 [][]에서 앞의 []는 벽돌 번호 그 뒤의 []는 벽돌 높이

    res = bricks[0][1];

    for i in range(1, n):
        max_h = 0;
        for j in range(i - 1, -1, -1):  # j는 i번째 벽돌 바로 밑에 애를 찾는거, i번쨰 벽돌이 내가 만들고자 하는 제일 상단
            if bricks[j][2] > bricks[i][2] and dy[j] > max_h:  # j번쨰는 i밑이니까 무게는 i보다 당연히 커야
                # dy[j]는  가장 상단이면서 그 상단인 탑중 최대를 찾는거.
                max_h = dy[j]
        dy[i] = max_h + bricks[i][1]  # max_h 이 값이 j번째 벽돌이 가장 위의최대 높이그리고 거기에 i번쨰 벽돌 더해줌
        # max_h가 j번쨰 벽돌이 가장위인 최대 높이에 새 벽돌 올려줌.
        # dy[i]는 i번쨰 벽돌이 제일 상단에 있는 탑이다.

        res = max(res, dy[i])

    print(res)
    return res;
print(solution(n,bricks));