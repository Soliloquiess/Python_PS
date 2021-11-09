import sys
# sys.stdin=open("input.txt", "r")

ans=[];
def DFS(L):
    global cnt
    if L==m:    #레벨이 m이되면 그대로 출력
        for i in range(m):
            print(res[i], end=' ')
            ans.append(res[i]);
        print()
        ans.append("ㄸ")
        cnt+=1
    else:
        for i in range(1, n+1):
            if ch[i]==0:    #체크변수 확인 0이면 적용 안 된거
                ch[i]=1     #적용해야되므로 1로 바꿈./
                res[L]=i
                DFS(L+1)    #호출하는거
                ch[i]=0     #되돌아와서 이 밑 하는거(1로 만들었던걸 0으로 만들어주고 실행)
    return cnt;
if __name__=="__main__":
    n, m=map(int, input().split())
    res=[0]*n
    ch=[0]*(n+1)
    cnt=0
    print(DFS(0));
    print(cnt)
    print(ans);
