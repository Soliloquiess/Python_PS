import sys
#sys.stdin=open("input.txt", "r")
def DFS(L):
    global cnt
    if L==m:
        for i in range(m):  #m까지 돌게(L까지 돌아도 되긴 함)
            print(res[i], end=' ')
        print()
        cnt+=1
    else:
        for i in range(1, n+1): #dfs가 0이였다면 여긴 dfs 1이 되서 n가닥 뻗어나가는거
            #n이 3이면 3번 호출하는거
            res[L]=i    #L자리에 i가 1이면 1 넣고 2면 2넣고
            DFS(L+1)

if __name__=="__main__":
    n, m=map(int, input().split())
    res=[0]*n
    cnt=0
    DFS(0)
    print(cnt)


