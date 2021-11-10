import sys
#sys.stdin=open("input.txt", "r")
#그래프는 항상 행->열 로 이동한다고 생각한다!
#g[a][b]=1 이면 a에서 b로 가는거 g[b][a]=1 면 b에서 a로 가는거
n,m= map(int, input().split());
ans = []
def solution(n,m):
    g=[[0]*(n+1) for _ in range(n+1)]   #n개 행열을 0으로 다 초기화
    for i in range(m):
        a, b , c=map(int, input().split())
        g[a][b]=c

        #a, b, c =map(int, input().split()) #c에 그래프의 가중치가 들어감.
        #g[a][b]=c   #이렇게 c를 넣어줘야 가중치 그래프가 된다.

    for i in range(1, n+1):
        for j in range(1, n+1):
            print(g[i][j], end=' ')
            ans.append(g[i][j]);
        print()
    return ans;
print(solution(n,m));