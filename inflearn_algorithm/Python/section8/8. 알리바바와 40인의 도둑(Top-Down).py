import sys


# sys.stdin = open("input.txt", 'r')
def DFS(x, y):
    if dy[x][y] > 0:  # 0보다 크면 방문했던거니까(값을 구한거니까) 메모이제이션
        return dy[x][y];  # 구한값을 바로 리턴함(메모이제이션) 시간 최적화를 위해 메모이제이션을 쓰자.

    if x == 0 and y == 0:  # 여기가 출발지점(재귀의 종료지점)
        return arr[0][0]  # 첫 출발점이 도착점이면


    else:  # 0,0이 출발점이 아닌 지점이면
        # 2가지 경우 생각 쭉위로 올라가거나 쭉 옆으로 가거나
        if y == 0:  # y가 0이란건 맨 왼쪽 0열의 지점(맨 왼쪽)
            dy[x][y] = DFS(x - 1, y) + arr[x][y]  # arr[x][y]  는 자기자신의 비용(자기자신 밟는거)
            # arr[x][y]  는 자기자신의 비용(자기자신 밟는거) dy[x][y]라는 테이블에 저장

            # DFS(x-1, y)왼쪽까지 오는거
            # return dy[x][y] = DFS(x - 1, y) + arr[x][y]
            # 근데 파이썬은 이렇게 바로 리턴을 못함

        elif x == 0:  # x가 0이란건 맨 위쪽 0행의 지점(맨 위쪽)
            dy[x][y] = DFS(x, y - 1) + arr[x][y]
            # arr[x][y]  는 자기자신의 비용(자기자신 밟는거) dy[x][y]라는 테이블에 저장

            # DFS(x, y-1)위쪽까지 오는거
            # DFS(x - 1, y)


        else:  # 두 갈래 길
            dy[x][y] = min(DFS(x - 1, y), DFS(x, y - 1)) + arr[x][y]
            # arr[x][y]  는 자기자신의 비용(자기자신 밟는거) dy[x][y]라는 테이블에 저장

            # DFS(x-1, y) 이게 바로 자기 위편까지 오는 최소비용 리턴받음
            # DFS(x, y - 1) 이게 바로 자기 왼편까지 오는 최소비용 리턴받음
            # 이 두개 값중 작은 값에 자기 비용(밟은 돌)을 더해주는거

        # 각자 리턴받은 값을 기록
        return dy[x][y]


if __name__ == "__main__":
    n = int(input())

    arr = [list(map(int, input().split())) for _ in range(n)]
    dy = [[0] * n for _ in range(n)]  # 메모이제이션 하기 위한 배열 잡음

    print(DFS(n - 1, n - 1))  # 이걸 도착지점으로 봄.

# top down은 재귀를 쓴다.(상태트리 사용)
# 상태트리에서 작은 값에 arr[]의 값을 더한다.