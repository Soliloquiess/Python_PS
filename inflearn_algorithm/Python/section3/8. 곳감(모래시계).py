import sys

# sys.stdin = open("input.txt", 'r')
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
m = int(input())
def solution(n,a,m):
    for i in range(m):  # m만큼 돔
        h, t, k = map(int, input().split())  #
        if (t == 0):  # t가 0이면 왼쪽으로 회전
            for _ in range(k):  # k개 만큼 회전
    # (a[h-1].pop(0)) 하면 젤 앞에꺼가 빠지고 떙겨짐.(deque이 아니고 list이기 떄문)
                a[h - 1].append(a[h - 1].pop(0))
    #h-1은 현재행(2행이면 1행이 컴퓨터에선 2행이므로 -1한거)
    #.append(a[h - 1].pop(0))     거기는 그 h-1행을 뺴는거(pop(0)이그 위치 팝하는거이므로)
    # (a[h-1].pop(0)) 하면 젤 앞에꺼가 빠지고 떙겨짐.(deque이 아니고 list이기 떄문)
    # 그리고  a[h-1].append(a[h-1].pop(0))로 맨 앞에꺼 뺸걸 뒤에 append

        else: #t가 1인 경우니까 오른쪽으로 돌고 위에 내용이랑 반대도는거.
            for _ in range(k):
                a[h - 1].insert(0, a[h - 1].pop()) # a[h - 1].pop() 그냥 넣어서 맨 뒤에서 뺸거.
    #그리고 insert(0이라 맨 앞에(0인덱스 자리에 넣는거)
    # insert 하고 위처럼 쓰면 0번 인덱스에 넣겠다는것
    # 그리고 pop()에 인덱스 안넣으면 젤 뒤에서 꺼냄
    # 그걸 그대로 0번 인덱스 앞에 넣는다는게 위 구문. 그럼 도는 효과 일어남.


    #이 아래 부분은 위에서 한 문제와 같음
    res = 0
    s = 0
    e = n - 1   #맨 끝 부분
    for i in range(n):
        for j in range(s, e + 1):
            res += a[i][j]
        if i < n // 2:
            # 좁혀들어가는거
            s += 1
            e -= 1
        else:
            # 다시 넓히는 거
            s -= 1
            e += 1
    # print(res)
    return res;

print(solution(n,a,m));