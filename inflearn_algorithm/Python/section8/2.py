import sys
#sys.stdin = open("input.txt", 'r')
#탑다운은 재귀와 메모이제이션 사용


def DFS(len):

    #여기서 가지 컷.dy[len]이 들어가 있으면 리턴해서 메모이제이션 적용한다(굉장히 중요)
    #메모이 제이션 안하면 다이나믹이 아님. 그냥 하면 재귀일 뿐.
    if dy[len] > 0:     #근데 무슨 값이 들어가면 0보다 큼
        return dy[len]  #그럼 기록 되어있으므로 바로 리턴(메모이제이션). 메모이제이션 하기떄문에 다이나믹 프로그래밍인거


    if len == 1 or len == 2:    #1,2,는 고정으로 1,2 리턴
        return len


    else:               #전 문제에서 했던거 그대로.
        dy[len] = DFS(len - 1) + DFS(len - 2)
        return dy[len]


if __name__ == "__main__":
    n = int(input())
    dy = [0] * (n + 1)      #처음엔 다 0으로 초기화
    print(DFS(n))



