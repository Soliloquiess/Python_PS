import sys

#sys.stdin = open("input.txt", "r")


def DFS(L, s, sum):
    global cnt
    if L == k:  #k개를 뽑아야 되는거 즉, dfs에서의 종착지점.
        if sum % m == 0:    #그 m의 배수가 되므로 카운트 +1
            cnt += 1
    else:
        for i in range(s, n):#여기서 i가 늘어나는 거고 이게 같은 레벨에서 옆으로 이동하는 거
            DFS(L + 1, i + 1, sum + a[i])   #이건 늘 하든 다음 트리노드 가는거.
           #L+1이 레벨 (트리 밑으로 내려가는거)
            #i+1이 옆으로 이동(같은 레벨의 다른 노드)
            #sum+a[i]는 각 노드들 합친 값.
            #L+1이 다음단계 i+1은 가지뻗은 값의 +1, a[i]는 뻗고자하는 그 값의 원소. 그걸 sum에 더한거.


if __name__ == "__main__":
    n, k = map(int, input().split())
    a = list(map(int, input().split())) #a라는 리스트에 n개의 자료를 저장
    m = int(input())    #m의 배수 찾는거
    cnt = 0
    DFS(0, 0, 0)
    print(cnt)